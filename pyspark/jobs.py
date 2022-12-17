from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType
from pyspark.udfs import get_english_name, get_start_year, get_trend
from pyspark.sql.functions import udf

class BirdsETLJob:
    input_path = 'birds.csv'

    def __init__(self):
        self.spark_session = (SparkSession.builder
                                          .master("local[1]")
                                          .appName("BirdsETLJob")
                                          .getOrCreate())

    def extract(self):
        input_schema = StructType([StructField("Species", StringType()),
                                   StructField("Category", StringType()),
                                   StructField("Period", StringType()),
                                   StructField("Annual percentage change", DoubleType())
                                   ])
        return self.spark_session.read.csv(self.input_path, header=True, schema=input_schema)

    def transform(self, df):
        get_english_name=udf(get_english_name, StringType())
        get_start_year=udf(get_start_year, IntegerType())
        get_trend=udf(get_trend, StringType())
        df=df.withColumn("Species", get_english_name(df.Species))
        df=df.withColumnRenamed("Species", "species")
        df=df.withColumnRenamed("Category", "category")
        df=df.withColumn("collected_from_year", get_start_year(df.Period))
        df=df.withColumnRenamed("Annual percentage change", "ann_percentage_change")
        df=df.withColumn("annual_percentage_change", df.ann_percentage_change)
        df=df.withColumn("trend", get_trend(df.annual_percentage_change))
        df=df.drop("Period","ann_percentage_change")
        return df
    def run(self):
        return self.transform(self.extract())
