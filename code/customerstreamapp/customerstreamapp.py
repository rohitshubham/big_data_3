import logging
import clientHistory 
from kafka import KafkaProducer
from datetime import datetime
from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils


custom_logging_format = '%(asctime)s : [%(levelname)s] - %(message)s'
logging.basicConfig(filename= "../../logs/mysimbdp_customerStreamApp.log" , filemode="a", level= logging.INFO, format = custom_logging_format)

topic = "mysimbdp"
topic_report = 'mysimbdp-clientReport'
broker = "localhost:9092"

#window duration in seconds
WINDOW_DURATION = 30

def GetKafkaProducer():
    return KafkaProducer(bootstrap_servers = [broker])

def send_alert(user_id, last_location):
    producer = GetKafkaProducer()
    producer.send(topic_report, str.encode(f'ALERT: user: {user_id} was found inactive at location {last_location}'))
    producer.flush()

def sendPartition(message):
    message.collect()

## The processing will we done on elements of each RDD due to .map method
## Each RDD will have the total messages received during the one window size 
def process(line):
    user = line.split(",")

    ## If there is issue in formatting date, time, we use datetime.now as we assume the time gap between sending and
    # receiving is not much.
    
    try:
        user_id = user[0]
        current_location = user[3]
        current_datetime = datetime.strptime(user[1] + " " + user[2], '%Y%m%d %H:%M:%S')
    except Exception as e:
        print(e)
        user_id = user[0]
        current_location = ''
        current_datetime = datetime.now()

    # We handle other errors gracefully, i.e. one error for a specific message, should not stop the operation
    try:
        if clientHistory.does_user_exist(user_id):
            data =  eval(clientHistory.get_client_history(user_id))
            print(data[0])
            last_location = data[0]
            last_datetime = datetime.strptime(data[1], '%Y%m%d %H:%M:%S')

            ## If the location has changes, we just update the value. Since, it means that person is still moving
            if last_location != current_location:
                clientHistory.save_client_history(user_id, current_location, user[1] + " " + user[2])

            ##Else we check the datetime of last movement
            else:
                gap_hours = abs((current_datetime - last_datetime).seconds) / 3600
                if last_location == 'kitchen' and gap_hours > 1:
                    send_alert(user_id, last_location)
                elif last_location == 'hall' and gap_hours > 2:
                    send_alert(user_id, last_location)
                elif last_location == 'livingroom' and gap_hours > 4:
                    send_alert(user_id, last_location)
                elif last_location == 'yard' and gap_hours > 1:
                    send_alert(user_id, last_location)
                elif last_location == 'bedroom' and gap_hours > 12:
                    send_alert(user_id, last_location)
        # We add new user to redis store        
        else: 
            clientHistory.save_client_history(user[0], current_location, user[1] + " " + user[2])
    except Exception as e:
        print(e)
    
logging.info("Starting Spark Streaming Context on Localhost")
sc = SparkContext("local[*]", "simpleAnalytics")
ssc = StreamingContext(sc, WINDOW_DURATION)
logging.info("Spark Streaming Context on localhost started")


logging.info(f"Attempting to connect to Kafka Broker on Topic: {topic} on broker: {broker}")
directKafkaStream = KafkaUtils.createDirectStream(ssc, [], {"metadata.broker.list": broker})
logging.info(f"Successfully connected to Kafka Broker on Topic: {topic} on broker: {broker}")


lines = directKafkaStream.map(lambda x: x[1])

processed_job = lines.map(process)
     

processed_job.foreachRDD(sendPartition)

logging.info(f"Starting analytics!")
ssc.start()
ssc.awaitTermination()