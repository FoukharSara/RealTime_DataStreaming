start containers with:
    `docker-compose up -d`
run 
`docker-compose run --rm airflow-webserver airflow db init`

run 
    `docker-compose run --rm airflow-webserver airflow users create --username admin --firstname Admin --lastname User --role Admin --email admin@example.com --password admin`
