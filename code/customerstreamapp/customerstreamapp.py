import logging
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils

custom_logging_format = '%(asctime)s : [%(levelname)s] - %(message)s'
logging.basicConfig(filename= "../../logs/mysimbdp_customerStreamApp.log" , filemode="a", level= logging.INFO, format = custom_logging_format)

logging.info("Starting Spark Streaming Context on Localhost")
sc = SparkContext("local[*]", "simpleAnalytics")
ssc = StreamingContext(sc, 20)
logging.info("Spark Streaming Context on localhost started")

topic = "mysimbdp"
broker = "localhost:9092"

logging.info(f"Attempting to connect to Kafka Broker on Topic: {topic} on broker: {broker}")
directKafkaStream = KafkaUtils.createDirectStream(ssc, [], {"metadata.broker.list": "localhost:9092"})
logging.info(f"Successfully connected to Kafka Broker on Topic: {topic} on broker: {broker}")


lines = directKafkaStream.map(lambda x: x[1])
counts = lines.flatMap(lambda line: line.split(",")) \
    .map(lambda word: (word, 1)) \
    .reduceByKey(lambda a, b: a+b)
counts.pprint()

logging.info(f"Starting analytics!")
ssc.start()
ssc.awaitTermination()