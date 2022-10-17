#!/bin/sh

chmod u+x wait-postgres.sh

while ! nc -z bmg_postgres_product_services 5432; do
    echo "Postgres is unavailable - sleeping"
    sleep 3;
done

echo "Postgres is up"