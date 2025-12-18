from pyspark import SparkConf, SparkContext
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: wordcount.py <input_hdfs_path> <output_hdfs_path>")
        sys.exit(1)
    input_path = sys.argv[1]
    output_path = sys.argv[2]

    conf = SparkConf().setAppName("WordCount")
    sc = SparkContext(conf=conf)
    text = sc.textFile(input_path)
    counts = (text.flatMap(lambda line: line.split())
                  .map(lambda w: (w.lower().strip(), 1))
                  .reduceByKey(lambda a,b: a+b))
    counts.saveAsTextFile(output_path)
    sc.stop()

if __name__ == "__main__":
    main()