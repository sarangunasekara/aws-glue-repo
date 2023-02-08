import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

sc = SparkContext.getOrCreate()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
data=spark.read.csv("s3://saran-g-bucket/dataset/input/usgs_main.csv",header=True,inferSchema=True)
data.describe()
data.groupby("type").count().show()
data.printSchema()
data.show(5,False)
data=data.na.drop()
data=data.drop("place","time","magSource")
data=data.withColumnRenamed("updated","time")
data=data.withColumnRenamed("locationSource","source")
data.show()
from pyspark.sql.functions import *
from pyspark.ml.feature import StringIndexer

l=["magType","net","type","source"]
#indexer=StringIndexer(inputCol=["magType","net","type","source"],outputCol=["magType1","net1","type1","source1"],handleInvalid="keep",stringOrderType="frequencyDesc")



indexer = [
StringIndexer(inputCol=c, outputCol="{0}1".format(c))
for c in l
]
from pyspark.ml import Pipeline
from pyspark.ml.regression import LinearRegression
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.sql.functions import unix_timestamp

# Convert the "time" column to the number of seconds since the Unix epoch
data = data.withColumn("time", unix_timestamp(data["time"]) / 1000)
va=VectorAssembler(inputCols=["latitude","longitude","depth","magType1","net1","mag","nst","time"],outputCol="features")

pipeline = Pipeline(stages=indexer + [va])
df_tfm=pipeline.fit(data).transform(data)
train, test = df_tfm.randomSplit([0.7, 0.3])
num_rows_train = train.count()
num_cols_train = len(train.columns)
print("Training:",num_rows_train,"x",num_cols_train)
num_rows_test = test.count()
num_cols_test = len(test.columns)
print("Training:",num_rows_test,"x",num_cols_test)
df_tfm.columns
scaler = StandardScaler(inputCol='features', outputCol='scaled_features')
scaler_model = scaler.fit(df_tfm)
train=scaler_model.transform(df_tfm)
test=scaler_model.transform(test)
train.show(3,False )
from pyspark.ml.classification import LogisticRegression
log=LogisticRegression(featuresCol='scaled_features',labelCol='type1')
lrmodel=log.fit(train)
prediction=lrmodel.transform(test)
test.show(3)
from pyspark.ml.evaluation import RegressionEvaluator
test.groupby("type").count().show()
train.groupby("type").count().show()
# Use the MulticlassClassificationEvaluator to evaluate the model's accuracy
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

evaluator = MulticlassClassificationEvaluator(labelCol="type1", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(prediction)
print("Accuracy:", accuracy)
# Select the "prediction" and "label" columns
predictions_df = prediction.select(["prediction", "type1"])

# Convert the predictions and labels to Pandas dataframes for easier inspection
predictions_pd = predictions_df.toPandas()

# Print the first 10 predictions and their corresponding true labels
print(predictions_pd.head(10))
# Set the hyperparameters for the logistic regression model
lr = LogisticRegression(labelCol='type1', featuresCol='features')

# Fit the model to the training data
lr_model = lr.fit(train)

# Make predictions on the test data
predictions = lr_model.transform(test)
# Save the model to a file
#lr_model.save("logistic_regression_model1")

# Load the saved model
#loaded_model = LogisticRegression.load("/content/logistic_regression_model1")

accuracy = evaluator.evaluate(predictions)
print("Accuracy:", accuracy)
from pyspark.ml.classification import RandomForestClassifier
rand=RandomForestClassifier(featuresCol='scaled_features',labelCol='type1')
rmodel=rand.fit(train)
predictionrand=rmodel.transform(test)
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

evaluator = MulticlassClassificationEvaluator(labelCol="type1", predictionCol="prediction", metricName="accuracy")
accuracy = evaluator.evaluate(predictionrand)
print("Accuracy:", accuracy)
# Select the "prediction" and "label" columns
predictions_df = predictionrand.select(["prediction", "type1"])

# Convert the predictions and labels to Pandas dataframes for easier inspection
predictions_pd = predictions_df.toPandas()

# Print the first 10 predictions and their corresponding true labels
print(predictions_pd.head(10))

# Set the hyperparameters for the logistic regression model
regrand = RandomForestClassifier(labelCol='type1', featuresCol='features',numTrees=100,maxDepth=5)

# Fit the model to the training data
regmodel = regrand.fit(train)

# Make predictions on the test data
predictions = regmodel.transform(test)

accuracy = evaluator.evaluate(predictions)
print("Accuracy:", accuracy)
from pyspark.ml.tuning import ParamGridBuilder, CrossValidator

# Define the hyperparameters to tune
hyperparameters = [
    {'regParam': [0.1, 0.01, 0.001], 'elasticNetParam': [0.0, 0.5, 1.0]},
    {'regParam': [0.1, 0.01, 0.001], 'elasticNetParam': [0.0, 0.5, 1.0], 'maxIter': [10, 50, 100]}
]
param_grid = ParamGridBuilder().addGrid(log.regParam, hyperparameters[0]['regParam'])\
                               .addGrid(log.elasticNetParam, hyperparameters[0]['elasticNetParam'])\
                               .build()
cv = CrossValidator(estimator=log, estimatorParamMaps=param_grid, evaluator=evaluator, numFolds=2)
model = cv.fit(train)
model.params
model.bestModel
predictions = model.transform(test)

accuracy = evaluator.evaluate(predictions)
print("Accuracy: ", accuracy)
job.commit()