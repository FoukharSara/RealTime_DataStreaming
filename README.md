start containers with:
    `docker-compose up -d`

run to start db
    `docker-compose run --rm airflow-webserver airflow db init`

run to create ur apache airflow account as login `admin` and password `admin`
    `docker-compose run --rm airflow-webserver airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com --password admin`

Architecture
    ![alt text](image.png)

    
