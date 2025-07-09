from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType

# Step 1: Spark session with Cassandra connector
spark = SparkSession.builder \
    .appName("KafkaToCassandra") \
    .config("spark.cassandra.connection.host", "cassandra") \
    .config("spark.cassandra.connection.port", "9042") \
    .getOrCreate()

# Step 2: Kafka schema
schema = StructType() \
    .add("first_name", StringType()) \
    .add("last_name", StringType()) \
    .add("gender", StringType()) \
    .add("address", StringType()) \
    .add("post_code", StringType()) \
    .add("email", StringType()) \
    .add("username", StringType()) \
    .add("dob", StringType()) \
    .add("registered_date", StringType()) \
    .add("phone", StringType()) \
    .add("picture", StringType())

# Step 3: Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "user_created") \
    .option("startingOffsets", "latest") \
    .load()

# Step 4: Parse JSON messages
json_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

# Step 5: Write to Cassandra
query = json_df.writeStream \
    .format("org.apache.spark.sql.cassandra") \
    .option("keyspace", "user_keyspace") \
    .option("table", "users") \
    .outputMode("append") \
    .option("checkpointLocation", "/tmp/checkpoint/user_data") \
    .start()

query.awaitTermination()
