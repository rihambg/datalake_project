# Projet 4 - Mini DataLake (Personne 1: Infrastructure & Docker)

But: Ce README explique comment démarrer l'infrastructure (HDFS + Spark) en local avec Docker Compose.

Prérequis
- Windows + WSL2 recommended
- Docker Desktop (avec Compose)
- Git
- Ports utilisés: 9870 (HDFS UI), 9000 (HDFS RPC), 8080 (Spark UI), 7077 (Spark master)

Structure du projet
- docker-compose.yml : orchestration multi‑conteneurs
- hadoop/* : fichiers de configuration HDFS
- spark/* : configuration spark env + script de soumission
- scripts/* : scripts pour initialiser HDFS, charger données et tester
- jobs/* : job Spark (wordcount.py)
- data/* : dataset exemple

Étapes pour lancer (PowerShell / WSL2)
1. Clonez le repo
   git clone <votre-repo> && cd projet4-datalake

2. Lancer Docker Compose
   docker compose up -d
   (ou `docker-compose up -d` si vous utilisez la vieille commande)

3. Initialiser/format HDFS et créer dossiers
   ./scripts/init-hdfs.sh

4. Charger données exemple dans HDFS
   ./scripts/put-sample-data.sh

5. Vérifier HDFS
   ./scripts/test-hdfs.sh
   Ouvrez http://localhost:9870 pour NameNode UI

6. Soumettre le job Spark (wordcount)
   ./spark/submit-wordcount.sh
   Vérifiez Spark UI: http://localhost:8080
   Vérifiez sortie dans HDFS: docker exec -it namenode bash -lc "hdfs dfs -ls -R /output"

Notes Windows
- Si des erreurs liées aux volumes apparaissent, lancez depuis WSL shell (Ubuntu) et assurez‑vous que Docker Desktop partage WSL.
- Vérifiez que les images existent localement ; si une image ne se télécharge pas, remplacez le tag par un tag disponible.

Dépannage rapide
- Voir logs d’un conteneur: docker logs -f namenode
- Entrer dans un conteneur: docker exec -it namenode bash
- Vérifier processus Java/Hadoop: jps

Fin README