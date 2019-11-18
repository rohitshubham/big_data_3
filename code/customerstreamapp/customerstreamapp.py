import logging
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from kafka import KafkaProducer

custom_logging_format = '%(asctime)s : [%(levelname)s] - %(message)s'
logging.basicConfig(filename= "../../logs/mysimbdp_customerStreamApp.log" , filemode="a", level= logging.INFO, format = custom_logging_format)

logging.info("Starting Spark Streaming Context on Localhost")
sc = SparkContext("local[*]", "simpleAnalytics")
ssc = StreamingContext(sc, 10)
logging.info("Spark Streaming Context on localhost started")

topic = "mysimbdp"
broker = "localhost:9092"

def GetKafkaProducer():
    return KafkaProducer(bootstrap_servers = [broker])


def sendPartition(message):
    records = message.collect()
    #producer = GetKafkaProducer()
    for record in records:
        print(record)
        #producer.send('mysimbdp-clientReport', str.encode(str(record)))
        #producer.flush()

def process(line):
    return line.split(",")

logging.info(f"Attempting to connect to Kafka Broker on Topic: {topic} on broker: {broker}")
directKafkaStream = KafkaUtils.createDirectStream(ssc, [], {"metadata.broker.list": "localhost:9092"})
logging.info(f"Successfully connected to Kafka Broker on Topic: {topic} on broker: {broker}")


lines = directKafkaStream.map(lambda x: x[1])
counts = lines.map(process)
     

counts.foreachRDD(sendPartition)
counts_alter = counts.reduceByKey(lambda a, b: a+b)

#counts_alter.foreachRDD(sendPartition)

logging.info(f"Starting analytics!")
ssc.start()
ssc.awaitTermination()