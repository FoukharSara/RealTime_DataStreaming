### Architecture
![alt text](image-1.png)
start containers with:
    `docker-compose up -d`

run to start db
    `docker-compose run --rm airflow-webserver airflow db init`

run to create ur apache airflow account as login `admin` and password `admin`
    `docker-compose run --rm airflow-webserver airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com --password admin`

    

### you have to run the producer twice cuz the first one time it creates the topic and for the second time it adds the message in messages

### to access the database u have to do this command
    `docker exec -it cassandra cqlsh`
    `$env:PYSPARK_PYTHON = "python"`

    
