spark-submit spark/streaming_pipeline.py


---

1. **`spark/data_ingestion.py`**
   ```python
   from pyspark.sql import SparkSession
   
   spark = SparkSession.builder.appName("Taxi Demand Prediction").getOrCreate()

   df = spark.readStream.format("kafka") \
       .option("kafka.bootstrap.servers", "localhost:9092") \
       .option("subscribe", "taxi_data") \
       .load()

   df.selectExpr("CAST(value AS STRING)").writeStream \
       .format("console") \
       .start() \
       .awaitTermination()