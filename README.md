# aws-glue-repo

 
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
