#!/bin/bash
# Usage: ./put-sample-data.sh
set -e
echo "Put sample data into HDFS (/input)"
docker exec -it namenode bash -lc "hdfs dfs -mkdir -p /input || true"
docker exec -it namenode bash -lc "hdfs dfs -put -f /opt/data/sample.txt /input/ || true"
echo "Listing /input:"
docker exec -it namenode bash -lc "hdfs dfs -ls -h /input || true"