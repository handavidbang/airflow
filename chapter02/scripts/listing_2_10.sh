#!/bin/bash

# Note: this script is a bit of a "hack" to run Airflow in a single container.
# This is obviously not ideal, but convenient for demonstration purposes.
# In a production setting, run Airflow in separate containers, as explained in Chapter 10.

# This is some weird as shit
set -x

# To turn it off 
# set + x 
#-v ${SCRIPT_DIR}/../dags/download_rocket_launches.py:/opt/airflow/dags/download_rocket_launches.py \

SCRIPT_DIR=$(cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd)

# docker run \
# -ti \
# -p 8080:8080 \
# -v ${SCRIPT_DIR}/../dags/download_rocket_launches.py:/opt/airflow/dags/download_rocket_launches.py \
# --name airflow
# --entrypoint=/bin/bash \
# apache/airflow:2.0.0-python3.8 \
# -c '( \
# airflow db init && \
# airflow users create --username admin --password admin --firstname Anonymous --lastname Admin --role Admin --email admin@example.org \
# ); \
# airflow webserver & \
# airflow scheduler \
# '


# Condensed version since I've been running into errors
docker run -ti -p 8080:8080 -v ${SCRIPT_DIR}/dags/download_rocket_launches.py:/opt/airflow/dags/download_rocket_launches.py --name airflow --entrypoint=/bin/bash apache/airflow:2.0.0-python3.8 -c '( \
airflow db init && \
airflow users create --username admin --password admin --firstname Anonymous --lastname Admin --role Admin --email admin@example.org \
); \
airflow webserver & \
airflow scheduler \
'