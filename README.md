# aws-glue-repo

## Authors

- [@sarangunasekara](https://www.github.com/sarangunasekara)


## Project Description:

The goal of this project is to build a model that can predict whether a hotel reservation will be cancelled or not based on the information provided in the above columns. The model will be trained on historical hotel reservation data and will use various factors such as number of adults, number of children, type of meal plan, lead time, market segment, previous cancellations, and other variables to make its predictions.


## Model Explanation

A classification model will be used to predict the hotel reservation cancellation status based on the data provided in the columns. The model will take in the various factors mentioned above as input and will output a prediction of either "cancelled" or "not cancelled". The model will be trained using supervised learning techniques, where it will learn the relationship between the input variables and the target variable (booking status) from a labeled training dataset. The model will be tested on a separate dataset to evaluate its accuracy.


## Outline

1. Data Preparation: The data will be loaded into a PySpark DataFrame and will undergo cleaning and pre-processing steps to remove missing values and handle categorical variables.

2. Feature Engineering: New features may be created by combining existing variables or by transforming variables to better capture the underlying relationships between the variables and the target variable.

3. Model Training: A suitable classification algorithm will be selected and the model will be trained on the cleaned and pre-processed data.

4. Model Evaluation: The model will be tested on a separate dataset to evaluate its accuracy and to identify any areas of improvement.

5. Model Deployment: The final model will be deployed in a production environment and will be used to make predictions on new hotel reservation data

