#!/bin/bash
# Minimal spark env that points Spark to the master and HADOOP conf
export SPARK_MASTER_HOST=spark-master
export SPARK_MASTER_PORT=7077
export SPARK_WORKER_CORES=1
export SPARK_WORKER_MEMORY=1g
export HADOOP_CONF_DIR=/etc/hadoop