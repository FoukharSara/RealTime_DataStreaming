import json 
from kafka import KafkaProducer
import time 
import requests
from airflow.operators.python import PythonOperator
from airflow import DAG

defalt_args = {
    'owner': 'airflow',
    start_date: datetime(2024, 11, 1,10,00)
}

def get_data():
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    data = res['results'][0]
    return data

def stream_data(): 
    #res = get_data()
    res = requests.get("https://randomuser.me/api/")
    res = res.json() 
    print(res)  
    
    
with DAG('kafka_stream',
         default_args=default_args,
         schedule_interval='@daily',
         catchup=False
    )as dag:
    
    streaming_task = PythonOperator(
        task_id='stream_data',
        python_callable=stream_data,
        dag=dag
    )
    
    

    