from pyspark.ml.feature import VectorAssembler
from pyspark.ml.regression import LinearRegression
from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("Taxi Demand Model Training").getOrCreate()

# Load processed data
df = spark.read.csv("data/processed/aggregated_data.csv", header=True, inferSchema=True)

# Feature engineering
assembler = VectorAssembler(inputCols=["hour", "day", "location"], outputCol="features")
data = assembler.transform(df).select("features", "demand")

# Train-test split
train_data, test_data = data.randomSplit([0.8, 0.2])

# Train model
lr = LinearRegression(featuresCol="features", labelCol="demand")
model = lr.fit(train_data)

# Save model
model.save("models/demand_model.pkl")
