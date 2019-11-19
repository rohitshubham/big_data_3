import logging
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
from kafka import KafkaProducer
import clientHistory 

custom_logging_format = '%(asctime)s : [%(levelname)s] - %(message)s'
logging.basicConfig(filename= "../../logs/mysimbdp_customerStreamApp.log" , filemode="a", level= logging.INFO, format = custom_logging_format)

logging.info("Starting Spark Streaming Context on Localhost")
sc = SparkContext("local[*]", "simpleAnalytics")
ssc = StreamingContext(sc, 10)
logging.info("Spark Streaming Context on localhost started")

topic = "mysimbdp"
broker = "localhost:9092"

client = clientHistory.Client

def GetKafkaProducer():
    return KafkaProducer(bootstrap_servers = [broker])


def sendPartition(message):
    records = message.collect()
    #producer = GetKafkaProducer()
    #for record in records:
    print(client.get_all_clients())
        #producer.send('mysimbdp-clientReport', str.encode(str(record)))
        #producer.flush()

def process(line):
    user = line.split(",")
    print(user[0],user[3], user[1] + user[2])
    if client.client_exists(user[0]):
        pass
    else:
        client.add_client(user[0],user[3], user[1] + user[2])
    

logging.info(f"Attempting to connect to Kafka Broker on Topic: {topic} on broker: {broker}")
directKafkaStream = KafkaUtils.createDirectStream(ssc, [], {"metadata.broker.list": "localhost:9092"})
logging.info(f"Successfully connected to Kafka Broker on Topic: {topic} on broker: {broker}")


lines = directKafkaStream.map(lambda x: x[1])
counts = lines.map(process)
     

counts.foreachRDD(sendPartition)

#counts_alter.foreachRDD(sendPartition)

logging.info(f"Starting analytics!")
ssc.start()
ssc.awaitTermination()