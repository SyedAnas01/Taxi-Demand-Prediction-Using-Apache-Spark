# Taxi-Demand-Prediction-Using-Apache-Spark
This project predicts real-time taxi demand using Apache Spark for big data processing and Spark MLlib for machine learning. The system ingests, processes, and analyzes streaming taxi ride data, forecasting demand hotspots to optimize resource allocation.


## Description
This project predicts real-time taxi demand using Apache Spark for big data processing and Spark MLlib for machine learning. The system ingests, processes, and analyzes streaming taxi ride data, forecasting demand hotspots to optimize resource allocation.

## Features
- **Real-Time Data Processing**: Ingests and processes streaming taxi data using Apache Kafka and Spark Streaming.
- **Data Transformation**: Cleanses and aggregates data with Spark SQL for trend analysis.
- **Machine Learning**: Trains a Spark MLlib regression model to predict taxi demand based on time and location.
- **Visualization**: Interactive dashboards built with Tableau and Power BI to visualize real-time and historical demand trends.

## Technologies Used
- **Big Data Framework**: Apache Spark (Streaming, SQL, MLlib)
- **Streaming Source**: Apache Kafka
- **Data Storage**: HDFS, Amazon S3
- **Programming Languages**: Python, SQL
- **Visualization**: Tableau, Power BI
- **Machine Learning**: Spark MLlib

## Repository Structure
- `data/`: Contains raw and processed datasets used in the project.
- `spark/`: Includes Python and SQL scripts for data ingestion, transformation, and demand prediction.
- `models/`: Machine learning models and training scripts.
- `kafka/`: Scripts for producing and consuming real-time data streams.
- `dashboards/`: Tableau dashboards and static visualizations.
- `docs/`: Project documentation and EDA analysis.

## Implementation
1. **Data Ingestion**:
   - Simulates real-time data streams using Kafka producers.
   - Streams ride data into Spark for processing.

2. **Data Processing**:
   - Cleans and aggregates data using Spark SQL.
   - Extracts meaningful features such as location, time, and trip distance.

3. **Machine Learning**:
   - Trains a demand prediction model with Spark MLlib using historical ride data.
   - Deploys the model to predict real-time demand on incoming streams.

4. **Visualization**:
   - Real-time dashboards showcasing demand trends and predictions.

## Usage
1. Start Kafka:
   ```bash
   kafka-server-start.sh config/server.properties
