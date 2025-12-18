#!/bin/bash
# Usage: ./submit-wordcount.sh
# Submits the wordcount job from Spark Master container
INPUT=hdfs://namenode:9000/input/sample.txt
OUTPUT=hdfs://namenode:9000/output/wordcount-$(date +%s)

echo "Submitting Spark job to spark://spark-master:7077"
docker exec -it spark-master bash -lc "/opt/spark/bin/spark-submit --master spark://spark-master:7077 /opt/spark/jobs/wordcount.py $INPUT $OUTPUT"
echo "Job submitted. When finished, check HDFS at: hdfs dfs -ls $OUTPUT"