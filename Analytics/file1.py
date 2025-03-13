

from pyspark.sql.functions import count, col, date_format, concat_ws,lit,hour
def Peak_Hours(tablename):
    df = tablename.withColumn('Hour', hour(tablename['order_time']))
    # result = df.groupBy('Hour').agg(count('order_id').alias('No_of_orders'))
    # result = result.orderBy(result.No_of_orders.desc())
    result = df.groupBy('Hour').agg(count('order_id').alias('No_of_orders'))
    result = result.orderBy(result.No_of_orders.desc())
    result = result.withColumn("formatted_hour", concat_ws(":", col("Hour"), lit("00")))
    df_with_12hr = result.withColumn("time_12hr", date_format(col("formatted_hour"), "hh:mm a"))
    df_with_12hr=df_with_12hr.select('No_of_orders','time_12hr')
    return df_with_12hr

