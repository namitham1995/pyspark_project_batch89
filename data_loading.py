from pyspark.sql import SparkSession
spark=SparkSession.builder.appName('Spark project').getOrCreate()
def Create_dataframe(Data,ishead):
    try:
        df = spark.read.csv(Data, header=ishead, inferSchema=True)
        return df
        print('---Dataframe created successfully---')
        print('***********************')
    except Exception as e:
        print(f'There is some error while creating table:{e}')
        print('***********************')