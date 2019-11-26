#!/bin/bash

#install docker 

sudo apt-get update

curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

sudo add-apt-repository \
   "deb [arch=amd64] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"

sudo apt-get install docker-ce docker-ce-cli containerd.io

sudo apt-get install docker-compose


#Add Spark context to the system- We need to use Java 8 and not Java 11.

export SPARK_HOME=~/spark-2.4.4-bin-hadoop2.7
export PYSPARK_PYTHON=python3
export PATH=$SPARK_HOME/bin:$PATH
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
PATH=$PATH:$HOME/bin:$JAVA_HOME/bin
export JAVA_HOME
export JAVA_HOME
export PATH

# Add python requrements
pip3 install -r ./requirements.txt 

# start the Kafka broker
sudo docker-compose -d ../mysimbdp-broker/ up

# Start redis instance 
sudo docker run -p 6379:6379 -d redis:latest

#Run the code
#This will automatically fetch Kafka streaming jar file from Maven Repo
spark-submit --packages  org.apache.spark:spark-streaming-kafka-0-8-assembly_2.11:2.4.4 ../customerstreamapp/customerstreamapp.py