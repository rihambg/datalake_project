#!/bin/bash
# small test: ls and cat
set -e
echo "HDFS root:"
docker exec -it namenode bash -lc "hdfs dfs -ls -R / || true"
echo "Cat sample file:"
docker exec -it namenode bash -lc "hdfs dfs -cat /input/sample.txt | sed -n '1,20p' || true"