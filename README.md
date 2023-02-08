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
    
## Hotel Reservation Dataset Overview:
----------------------------------------
- Columns are : ['Booking_ID', 'no_of_adults', 'no_of_children', 'no_of_weekend_nights', 'no_of_week_nights', 'type_of_meal_plan', 'required_car_parking_space', 'room_type_reserved', 'lead_time', 'arrival_year', 'arrival_month', 'arrival_date', 'market_segment_type', 'repeated_guest', 'no_of_previous_cancellations', 'no_of_previous_bookings_not_canceled', 'avg_price_per_room', 'no_of_special_requests', 'booking_status']

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
