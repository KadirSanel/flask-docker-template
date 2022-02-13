#!/usr/bin/env bash

if [ "$1" == "build" ]
then
    docker build -t api_service .
fi

if [ "$1" == "runserver" ]
then
    docker run -d -p 5000:5000 api_service
fi

if [ "$1" == "stopall" ]
then
    docker kill $(docker ps -q)
fi

if [ "$1" == "createdb" ]
then
    systemctl stop postgresql
    docker run --name api_db -e POSTGRES_PASSWORD=api_db -d -p 5432:5432 -v /volumes/api_db/data:/var/lib/postgresql/data  postgres
fi

if [ "$1" == "rundb" ]
then
    systemctl stop postgresql
    docker start api_db
fi

if [ "$1" == "stopdb" ]
then
    systemctl stop postgresql
    docker stop api_db
fi

if [ "$1" == "removedb" ]
then
    systemctl stop postgresql
    docker stop api_db
    docker rm api_db
fi

if [ "$1" == "migrate" ]
then
    python3 src/manage.py migrate
fi

if [ "$1" == "install" ]
then
    apt-get install docker
    apt-get install tesseract-python
    apt-get install opencv-python
    pip install -r requirements.txt
fi
