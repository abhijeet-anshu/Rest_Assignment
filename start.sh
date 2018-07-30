#!/bin/bash

port=8000
#Apply migrations 
echo [`date "+%Y-%m-%d %T"` +0000] [$$] check migrations
python manage.py makemigrations
echo [`date "+%Y-%m-%d %T"` +0000] [$$] Apply migrations
python manage.py migrate

#Load data from csv
echo [`date "+%Y-%m-%d %T"` +0000] [$$] Command to start server on port
echo [`date "+%Y-%m-%d %T"` +0000] [$$] Read data from csv
python manage.py shell --plain < loaddata.py

# Start Gunicorn processes
echo Starting Gunicorn.
exec gunicorn rest_assignment.wsgi:application \
    --bind 0.0.0.0:$port \
    --workers 3
