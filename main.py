from ucimlrepo import fetch_ucirepo
import pandas as pd
import findspark
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.feature import VectorAssembler, StandardScaler
from pyspark.ml.regression import LinearRegression

# Initialize Spark
findspark.init()
spark = SparkSession.builder.appName("Airfoil ML Pipeline").getOrCreate()

# Fetch the dataset
dataset = fetch_ucirepo(id=291)

features = dataset.data.features
target = dataset.data.targets
df1 = pd.DataFrame(features)
df2 = pd.DataFrame(target)

combined_data = pd.concat([df1, df2], axis=1)

# Convert to Spark DataFrame
spark_df = spark.createDataFrame(combined_data)

# Transform Dataframe
spark_df = spark_df.dropna()
spark_df = spark_df.drop_duplicates()
spark_df = spark_df.withColumnRenamed("scaled-sound-pressure", "sound-level-decibels")

# Save the DataFrame to a file
spark_df.write.mode("overwrite").csv("airfoil_data.csv", header=True)

# Define the pipeline stages
featureColumns = [
    "frequency",
    "attack-angle",
    "chord-length",
    "free-stream-velocity",
    "suction-side-displacement-thickness",
]
assembler = VectorAssembler(inputCols=featureColumns, outputCol="features")
scaler = StandardScaler(inputCol="features", outputCol="scaled-features")
lr = LinearRegression(featuresCol="scaled-features", labelCol="sound-level-decibels")

# Create the pipeline
pipeline = Pipeline(stages=[assembler, scaler, lr])

# Split the data into training and test sets
(training_data, testing_data) = spark_df.randomSplit([0.7, 0.3], seed=42)

# Fit the pipeline model
pipeline_model = pipeline.fit(training_data)

# Make predictions
predictions = pipeline_model.transform(testing_data)

# Evaluate the model
# RMSE
evaluator = RegressionEvaluator(
    labelCol="sound-level-decibels", predictionCol="prediction", metricName="rmse"
)
rmse = evaluator.evaluate(predictions)
print(f"Root Mean Squared Error (RMSE): {rmse}")

# R2
evaluator = RegressionEvaluator(
    labelCol="sound-level-decibels", predictionCol="prediction", metricName="r2"
)
r2 = evaluator.evaluate(predictions)
print(f"R2: {r2}")

# MAE
evaluator = RegressionEvaluator(
    labelCol="sound-level-decibels", predictionCol="prediction", metricName="mae"
)
mae = evaluator.evaluate(predictions)
print(f"Mean Absolute Error (MAE): {mae}")

# Save the model
pipeline_model.write().save("airfoil_model")

# Stop the Spark session
spark.stop()
