#!/bin/bash

if [ "$DATABASE" = "postgres" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

export PYTHONPATH=/usr/src/app/triumph/;$PYTHONPATH

cd /usr/src/app/triumph

python manage.py makemigrations
python manage.py migrate
python manage.py initadmins
python manage.py collectstatic --no-input

exec "$@"