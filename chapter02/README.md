# Chapter 2

Code accompanying Chapter 2 of the book [Data Pipelines with Apache Airflow](https://www.manning.com/books/data-pipelines-with-apache-airflow).

## Contents

This folder contains DAGs from Chapter 2. The filenames and DAG ids follow the listing ids in the book. The
final DAG is given in `listing_2_10.py`.

## Usage

To get started with the code examples, start Airflow with Docker Compose with the following command:

```bash
docker-compose up -d
```

NOTE: WAIT A WHILE SINCE IT MIGHT TAKE SOME TIME TO LOAD

The webserver initializes a few things, so wait for a few seconds, and you should be able to access the
Airflow webserver at http://localhost:8080.

To stop running the examples, run the following command:

```bash
docker-compose down -v
```

## Getting started 

This is p. 29 

```bash 
pip install apache-airflow 

airflow db init 
airflow users create --username admin --password admin --firstname First --lastname Last --role Admin --email admin@email.com
cp download_rocket_launches.py ~/airflow/dags/ 
airflow webserver 
airflow scheduler
```

## Run THIS SEPARTELY i.e. don't do the instructions above

## Running Airflow in Docker containers

This is on p.30

```bash
docker run -ti -p 8080:8080 -v ${SCRIPT_DIR}/dags/download_rocket_launches.py:/opt/airflow/dags/download_rocket_launches.py --name airflow --entrypoint=/bin/bash apache/airflow:2.0.0-python3.8 -c '( \
airflow db init && \
airflow users create --username admin --password admin --firstname Anonymous --lastname Admin --role Admin --email admin@example.org \
); \
airflow webserver & \
airflow scheduler \
'
```

NOTE: WAIT A WHILE THEN go to http://localhost:8080

Run the DAG then to check the images go into the Docker container 

```bash
docker exec -it airflow /bin/bash
```

Then go into "/tmp/images" directory 

```bash
cd ~/tmp/images
```

### Checking containers 
Look for "airflow" under Names 
```bash
docker ps -a
```

