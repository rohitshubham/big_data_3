# Deployment 3

### CS-E4640 Big data platforms 
#### Rohit Raj - 801636
---

This assignment has 4 components that we need to deploy:
* mysimbdp-broker (_Kafka Broker_)
* Redis
* Apache Spark Streaming
* ClientStreamProcessing Application

You will need root access to install components and run docker. All the docker images are by default pulled from `docker-hub` and run on `tag:latest`.

Deployed of all these 4 components can be done with a single script present in `/code/scripts/script.sh`. Just run the command

```shell
$ sudo bash /code/scripts/script.sh
```

This single script will install and run all the 4 components.

---

To start insertion of data from /data/data.csv, into the Kafka ingestion queue, run the python script:

```shell
$ python3 /code/mysimbdp-broker/connect_to_kafka.py
```

Similarly to listen to the results sent by spark stream processing, run the python script:

```shell
$ python3 /code/mysimbdp-broker/kafka_consumer.py
``` 

no container is required for these scripts.
