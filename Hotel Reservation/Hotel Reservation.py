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
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.feature import VectorAssembler, StringIndexer
from pyspark.ml.classification import LogisticRegression
from pyspark.ml.evaluation import BinaryClassificationEvaluator
S3_Path = "s3://saran-g-bucket/hotel-reservation/input/Hotel Reservations.csv"
data = (
    spark.read.format("org.apache.spark.csv")
    .option("header", True)
    .option("quote", '"')
    .option("escape", '"')
    .option("inferSchema", True)
    .option("ignoreLeadingWhiteSpace", True)
    .option("ignoreTrailingWhiteSpace", True)
    .csv(S3_Path, multiLine=False)
)
print('Total Size: '+ str(data.count())+' x '+str(len(data.columns)))
data.printSchema()
data.columns
data.show(5,False)
data= data.dropna()
data = data.select(
  "no_of_adults",
  "no_of_children",
  "no_of_weekend_nights",
  "no_of_week_nights",
  "type_of_meal_plan",
  "required_car_parking_space",
  "room_type_reserved",
  "lead_time",
  "arrival_year",
  "arrival_month",
  "market_segment_type",
  "repeated_guest",
  "no_of_previous_cancellations",
  "no_of_previous_bookings_not_canceled",
  "avg_price_per_room",
  "no_of_special_requests",
  "booking_status"
)
from pyspark.ml import Pipeline
from pyspark.ml.feature import StringIndexer, OneHotEncoder

# Create a list of the string columns to be converted
string_columns = ["type_of_meal_plan", "room_type_reserved", "market_segment_type" , 'booking_status']

# Create a list to store the indexers
indexers = []

# Loop through the string columns and create an indexer for each one
for col in string_columns:
    indexer = StringIndexer(inputCol=col, outputCol=col + "_indexed")
    indexers.append(indexer)

numerical_columns = ["no_of_adults", "no_of_children", "no_of_weekend_nights", "no_of_week_nights",
                     "required_car_parking_space", "lead_time", "arrival_year", "arrival_month",
                     "repeated_guest", "no_of_previous_cancellations", "no_of_previous_bookings_not_canceled",
                     "avg_price_per_room", "no_of_special_requests"] + [col + "_indexed" for col in string_columns]
vector_assembler =VectorAssembler(inputCols=numerical_columns, outputCol="features")

# Create a pipeline that includes all the indexers and encoders
pipeline = Pipeline(stages=indexers+[vector_assembler])

# Fit the pipeline on the input data
model = pipeline.fit(data)

# Use the transform method on the pipeline to convert the string columns
encoded_data = model.transform(data)
encoded_data.printSchema
#df.columns
encoded_data.columns
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import BinaryClassificationEvaluator

# Split the data into training and testing sets
train_df, test_df = encoded_data.randomSplit([0.7, 0.3], seed=42)

# Create an instance of the RandomForestClassifier class
rf = RandomForestClassifier(labelCol="booking_status_indexed", featuresCol="features")

# Fit the random forest classifier on the training data
rmodel = rf.fit(train_df)

# Use the transform method of the model to make predictions on the testing data
rpredictions = rmodel.transform(test_df)
from pyspark.ml.classification import LogisticRegression

# Create an instance of the LogisticRegression class
lr = LogisticRegression(labelCol="booking_status_indexed", featuresCol="features")

# Fit the logistic regression model on the training data
lmodel = lr.fit(train_df)

# Use the transform method of the model to make predictions on the testing data
lpredictions = lmodel.transform(test_df)
from pyspark.ml.classification import GBTClassifier

# Create an instance of the GBTClassifier class
gbt = GBTClassifier(labelCol="booking_status_indexed", featuresCol="features")

# Fit the gradient-boosted tree classifier on the training data
gmodel = gbt.fit(train_df)

# Use the transform method of the model to make predictions on the testing data
gpredictions = gmodel.transform(test_df)
from pyspark.ml.classification import DecisionTreeClassifier

# Split the data into training and testing sets
train_df, test_df = encoded_data.randomSplit([0.7, 0.3], seed=42)

# Create an instance of the DecisionTreeClassifier class
dt = DecisionTreeClassifier(labelCol="booking_status_indexed", featuresCol="features")

# Fit the decision tree classifier on the training data
dmodel = dt.fit(train_df)

# Use the transform method of the model to make predictions on the testing data
dpredictions = dmodel.transform(test_df)
# Evaluate the model using the BinaryClassificationEvaluator
evaluator = BinaryClassificationEvaluator(labelCol="booking_status_indexed", rawPredictionCol="prediction", metricName="areaUnderROC")
raccuracy = evaluator.evaluate(rpredictions)
laccuracy = evaluator.evaluate(lpredictions)
gaccuracy = evaluator.evaluate(gpredictions)
daccuracy = evaluator.evaluate(dpredictions)
print("Random Forest Accuracy:", raccuracy)
print("Random Forest Accuracy:", raccuracy)
print("Logistic Regression Accuracy:", raccuracy)
print("GBT Classifier Accuracy:", raccuracy)
print("Decision Tree Accuracy:", raccuracy)

from pyspark.ml.evaluation import MulticlassClassificationEvaluator

evaluator = MulticlassClassificationEvaluator(labelCol="booking_status_indexed", predictionCol="prediction", metricName="accuracy")

predictions_df = dpredictions.select(["prediction", "booking_status_indexed"])

# Convert the predictions and labels to Pandas dataframes for easier inspection
predictions_pd = predictions_df.toPandas()

# Print the first 10 predictions and their corresponding true labels
print(predictions_pd.head(10))

try:
    model.write().overwrite().save("s3://saran-g-bucket/hotel-reservation/output/")
except Exception as e:
    print("Error saving model to S3: {}".format(e))

job.commit()