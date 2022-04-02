"""DAG demonstrating the umbrella use case with dummy operators."""

import airflow.utils.dates
from airflow import DAG
from airflow.operators.dummy import DummyOperator
from airflow.operators.python import PythonOperator
from pathlib import Path 
import os 
import sys
import numpy as np
import pickle
import logging
from datetime import datetime

dag = DAG(
    dag_id="die_simulations",
    description="Simulate dies on a daily scedule",
    start_date=datetime(2022, 3, 29),
    end_date=datetime(2022, 5, 1),
    schedule_interval="@hourly",
)

FILEPATH = Path().absolute() / 'data.pickle'

def open_simulated_logs(filename=FILEPATH):
    """Unpickles the data set"""
    try:
        with open(filename, 'rb') as f:
            base = pickle.load(f)
    except FileNotFoundError:
        with open(filename, 'wb') as f:
            base = np.random.randint(1,7, size=(1,6))
            pickle.dump(base, f)
    return base 

def update_simulated_logs(base, filename=FILEPATH):
    """Updates the data set"""
    data = np.random.randint(1,7, size=(1,6))
    with open(filename, 'wb') as f:
        combine = [base, data]
        base = np.concatenate(combine, axis=0)
        pickle.dump(base, f)
    return 


open_or_create = PythonOperator(task_id='open_file',python_callable=open_simulated_logs, dag=dag)
simulate = PythonOperator(task_id='simulate',python_callable=update_simulated_logs, dag=dag)

open_or_create >> simulate

# def simulate_die_rolls(filename, n=10):
#     """Simulate and roll it 10 times"""
#     for i in range(n):
#         base = open_simulated_logs(filename)
#         update_simulated_logs(base, filename)
#     return

    







# # Data collection 
# fetch_weather_forecast = DummyOperator(task_id="fetch_weather_forecast", dag=dag)
# fetch_sales_data = DummyOperator(task_id="fetch_sales_data", dag=dag)

# # Cleaning process 
# clean_forecast_data = DummyOperator(task_id="clean_forecast_data", dag=dag)
# clean_sales_data = DummyOperator(task_id="clean_sales_data", dag=dag)

# # Merge data
# join_datasets = DummyOperator(task_id="join_datasets", dag=dag)

# # Model development + deployment
# train_ml_model = DummyOperator(task_id="train_ml_model", dag=dag)
# deploy_ml_model = DummyOperator(task_id="deploy_ml_model", dag=dag)

# # Set dependencies between all tasks

# # Fetch weather data 
# fetch_weather_forecast >> clean_forecast_data

# # Fetch sales data
# fetch_sales_data >> clean_sales_data

# # Join data 
# [clean_forecast_data, clean_sales_data] >> join_datasets

# # Model process
# join_datasets >> train_ml_model >> deploy_ml_model
