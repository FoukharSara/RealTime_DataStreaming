import json 
from kafka import KafkaProducer
import time 
import requests
from airflow.operators.python import PythonOperator
from airflow import DAG
from datetime import datetime
import logging


default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 11, 1,10,00)
}

def get_data():
    res = requests.get("https://randomuser.me/api/")
    res = res.json()
    data = res['results'][0]
    return data

def format_data(res):
    data = {}
    location = res['location']
    # data['id'] = uuid.uuid4()
    data['first_name'] = res['name']['first']
    data['last_name'] = res['name']['last']
    data['gender'] = res['gender']
    data['address'] = f"{str(location['street']['number'])} {location['street']['name']}, " \
                      f"{location['city']}, {location['state']}, {location['country']}"
    data['post_code'] = location['postcode']
    data['email'] = res['email']
    data['username'] = res['login']['username']
    data['dob'] = res['dob']['date']
    data['registered_date'] = res['registered']['date']
    data['phone'] = res['phone']
    data['picture'] = res['picture']['medium']

    return data

def stream_data():
    producer = KafkaProducer(bootstrap_servers=['broker:29092'],max_block_ms=5000)
    curr_time = time.time()
    
    while True:
        if time.time() - curr_time > 60:
            break
        try:
            res = get_data()
            res = format_data(res) 
            #print(json.dumps(res, indent=3))
            producer.send('user_created', json.dumps(res).encode('utf-8'))
        
        except Exception as e:
            logging.error(f"Error: {e}")
            continue

            
     
    
    
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
    
    

    