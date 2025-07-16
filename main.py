from ucimlrepo import fetch_ucirepo
import pandas as pd
import findspark
from pyspark.sql import SparkSession
from pyspark.ml import Pipeline
from pyspark.ml.pipeline import PipelineModel
from pyspark.ml.feature import StringIndexer, VectorAssembler, StandardScaler
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
print(combined_data)
