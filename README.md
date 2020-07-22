# National Park Trails :sunrise_over_mountains:

National Park Trails data that is loaded into a database for analysis using Apache Cassandra.

### Project Structure
```
Car-Accidents-ETL
| README.md
| 
└─── data
| | alltrails-nationalpark.csv # dataset of all national park trails in the U.S. 
|
└─── src # code for ETL
| | etl_helper.pynb # notebook to help setup ETL
| | perform_etl.py # performs ETL to load national park trail data
| | sql_queries.py # contains drop, insert, create, and read statements
|
└─── visualize (in progress) # visualize national park trails data using d3.js
```
