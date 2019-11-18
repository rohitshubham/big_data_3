#!/bin/bash

#Add Spark
export SPARK_HOME=~/spark-2.4.4-bin-hadoop2.7
export PYSPARK_PYTHON=python3
export PATH=$SPARK_HOME/bin:$PATH
JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
PATH=$PATH:$HOME/bin:$JAVA_HOME/bin
export JAVA_HOME
export JAVA_HOME
export PATH


#Run the code
#This will automatically fetch Kafka streaming jar file from Maven Repo
spark-submit --packages  org.apache.spark:spark-streaming-kafka-0-8-assembly_2.11:2.4.4 ../customerstreamapp/customerstreamapp.py