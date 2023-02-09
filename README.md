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

---------------------------
To create an orchestration pipeline for training and inference in Apache Spark using AWS Glue, follow these steps:
   1. Start by creating a Glue job in the AWS Glue console.
   2. Define the job parameters, including the name of the job, the IAM role to be used, and the number of worker nodes.
   3. Define the source data either by connecting to an Amazon S3 bucket or pointing to a file in the Glue data catalog.
   4. Use Spark's data processing capabilities to clean and preprocess the data.
   5. Train a machine learning model on the preprocessed data using the Spark MLlib library.
   6. Store the trained model in an Amazon S3 bucket for later use.
   7. Define a new task in AWS Glue that performs inference using the stored model.
   8. Connect the inference task to the output of the data processing stage to make predictions on new data.
   9. Store the predictions in an Amazon S3 bucket or in the Glue data catalog.
   10. Finally, monitor the performance of the pipeline and make necessary adjustments to optimize the accuracy of the predictions.

This outline provides a general approach for creating an orchestration pipeline for training and inference in Apache Spark using AWS Glue, with the exact steps varying depending on the specific requirements of the use case.

To perform this, I've used two different datasets:
    - USGS dataset
    - Hotel Reservation

- Schema :
   ```bash 
        root
         |-- Booking_ID: string (nullable = true)
         |-- no_of_adults: integer (nullable = true)
         |-- no_of_children: integer (nullable = true)
         |-- no_of_weekend_nights: integer (nullable = true)
         |-- no_of_week_nights: integer (nullable = true)
         |-- type_of_meal_plan: string (nullable = true)
         |-- required_car_parking_space: integer (nullable = true)
         |-- room_type_reserved: string (nullable = true)
         |-- lead_time: integer (nullable = true)
         |-- arrival_year: integer (nullable = true)
         |-- arrival_month: integer (nullable = true)
         |-- arrival_date: integer (nullable = true)
         |-- market_segment_type: string (nullable = true)
         |-- repeated_guest: integer (nullable = true)
         |-- no_of_previous_cancellations: integer (nullable = true)
         |-- no_of_previous_bookings_not_canceled: integer (nullable = true)
         |-- avg_price_per_room: double (nullable = true)
         |-- no_of_special_requests: integer (nullable = true)
         |-- booking_status: string (nullable = true)
     ```
     
## USGS Dataset Overview:
----------------------------------------
- Schema:
   ```bash
        root
         |-- time: timestamp (nullable = true)
         |-- latitude: double (nullable = true)
         |-- longitude: double (nullable = true)
         |-- depth: double (nullable = true)
         |-- mag: double (nullable = true)
         |-- magType: string (nullable = true)
         |-- nst: double (nullable = true)
         |-- gap: double (nullable = true)
         |-- dmin: double (nullable = true)
         |-- rms: double (nullable = true)
         |-- net: string (nullable = true)
         |-- id: string (nullable = true)
         |-- updated: timestamp (nullable = true)
         |-- place: string (nullable = true)
         |-- type: string (nullable = true)
         |-- horizontalError: double (nullable = true)
         |-- depthError: double (nullable = true)
         |-- magError: double (nullable = true)
         |-- magNst: double (nullable = true)
         |-- status: string (nullable = true)
         |-- locationSource: string (nullable = true)
         |-- magSource: string (nullable = true)
    ```   
         
The two different datasets have been used to perform different operations and workflows. And tried to do this with jupyter notebook and by graph through visual interactive console for learning practise.

The project overview, description and outline describes a dataset related to earthquake data collected by the US Geological Survey (USGS). The dataset contains information about various attributes of earthquakes such as time, location, magnitude, depth, and source, among others. Each attribute is represented as a field with a data type, such as double or string, and some fields may contain null values. The project can be used to perform data analysis and gain insights into earthquakes, including their frequency, location, and severity. An outline of the project could include steps such as loading the data into a database, cleaning and pre-processing the data, and performing data analysis and visualization to generate meaningful insights.
