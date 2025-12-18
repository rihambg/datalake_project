from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum as spark_sum, count, avg, desc

# Creer session Spark
spark = SparkSession.builder \
    .appName("Sales Analysis") \
    .getOrCreate()


print("ANALYSE DES VENTES - Mini DataLake")


# Lire les donnees depuis HDFS
print("\n1. Chargement des donnees depuis HDFS...")
df = spark.read.csv(
    "hdfs://namenode:9000/user/data/raw/sales_data_sample.csv",
    header=True,
    inferSchema=True
)

# Afficher schema
print("\n2. Schema des donnees:")
df.printSchema()

# Compter lignes
total_rows = df.count()
print("\n3. Nombre total de lignes: " + str(total_rows))

# Apercu
print("\n4. Apercu des donnees:")
df.show(5)

# ANALYSE 1: Ventes par pays
print("\n5. ANALYSE 1: Ventes totales par pays")
sales_by_country = df.groupBy("COUNTRY") \
    .agg(
        spark_sum("SALES").alias("TOTAL_SALES"),
        count("ORDERNUMBER").alias("NB_ORDERS")
    ) \
    .orderBy(desc("TOTAL_SALES"))

sales_by_country.show(10)

# Sauvegarder
print("\n   Sauvegarde dans HDFS...")
sales_by_country.coalesce(1).write.mode("overwrite").csv(
    "hdfs://namenode:9000/user/data/results/sales_by_country",
    header=True
)
print("    Sauvegarde dans /user/data/results/sales_by_country")

# ANALYSE 2: Top produits
print("\n6. ANALYSE 2: Top 10 produits")
top_products = df.groupBy("PRODUCTLINE") \
    .agg(
        spark_sum("QUANTITYORDERED").alias("TOTAL_QUANTITY"),
        spark_sum("SALES").alias("TOTAL_REVENUE")
    ) \
    .orderBy(desc("TOTAL_QUANTITY"))

top_products.show(10)

# Sauvegarder
print("\n   Sauvegarde dans HDFS...")
top_products.coalesce(1).write.mode("overwrite").csv(
    "hdfs://namenode:9000/user/data/results/top_products",
    header=True
)
print("    Sauvegarde dans /user/data/results/top_products")

# ANALYSE 3: Ventes par trimestre
print("\n7. ANALYSE 3: Ventes par trimestre")
sales_by_quarter = df.groupBy("YEAR_ID", "QTR_ID") \
    .agg(
        spark_sum("SALES").alias("TOTAL_SALES"),
        count("ORDERNUMBER").alias("NB_ORDERS")
    ) \
    .orderBy("YEAR_ID", "QTR_ID")

sales_by_quarter.show()

# Sauvegarder
print("\n   Sauvegarde dans HDFS...")
sales_by_quarter.coalesce(1).write.mode("overwrite").csv(
    "hdfs://namenode:9000/user/data/results/sales_by_quarter",
    header=True
)
print("   Sauvegarde dans /user/data/results/sales_by_quarter")

# ANALYSE 4: Top clients
print("\n8. ANALYSE 4: Top 10 clients")
top_customers = df.groupBy("CUSTOMERNAME", "COUNTRY") \
    .agg(
        spark_sum("SALES").alias("TOTAL_SPENT"),
        count("ORDERNUMBER").alias("NB_ORDERS")
    ) \
    .orderBy(desc("TOTAL_SPENT"))

top_customers.show(10, truncate=False)

# Sauvegarder
print("\n   Sauvegarde dans HDFS...")
top_customers.coalesce(1).write.mode("overwrite").csv(
    "hdfs://namenode:9000/user/data/results/top_customers",
    header=True
)
print("    Sauvegarde dans /user/data/results/top_customers")


print("ANALYSE TERMINEE AVEC SUCCES !")


# Arreter Spark
spark.stop()