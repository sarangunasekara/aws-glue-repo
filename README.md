# aws-glue-repo

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

