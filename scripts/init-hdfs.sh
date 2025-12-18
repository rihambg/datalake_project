#!/bin/bash
# Usage: ./init-hdfs.sh
set -e

echo "Waiting for namenode to be ready..."
sleep 5

# Format the namenode only if needed. We try and ignore if already formatted.
if docker exec namenode bash -lc "[ ! -d /hadoop/dfs/name/current ]"; then
  echo "Formatting namenode..."
  docker exec -it namenode bash -lc "hdfs namenode -format -force -nonInteractive || true"
else
  echo "Namenode already formatted"
fi

echo "Starting HDFS daemons inside containers (if not already started)..."
# For these images, the daemons are started by container entrypoints.
# Just show statuses:
docker exec namenode bash -lc "jps || true"
docker exec datanode bash -lc "jps || true"

echo "Creating HDFS directories (/user and /tmp)"
docker exec -it namenode bash -lc "hdfs dfs -mkdir -p /user/$(whoami) || true"
docker exec -it namenode bash -lc "hdfs dfs -mkdir -p /tmp || true"
docker exec -it namenode bash -lc "hdfs dfs -chmod -R 1777 /tmp || true"

echo "HDFS init done. Check NameNode UI at http://localhost:9870"