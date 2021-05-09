#! /bin/bash

#set -e

if [ "$1" == "help" ]; then
  echo "./build.sh help      <-  help"
  echo "./build.sh start     <-  start docker compose"
  echo "./build.sh stop      <-  stop docker compose"
  echo "./build.sh populate  <-  populate database tables"
  exit
fi

if [ "$1" == "populate" ]; then
  docker exec $(docker ps | grep flask | cut -d " " -f1 | head -1) python3 populateTables.py

  exit
fi

echo Exit Docker Swarm
sudo docker swarm leave --force
sleep 1
if [ "$1" != "stop" ]; then
  echo Init Docker Swarm
  sudo docker swarm init
fi
sleep 1

if [ "$1" != "stop" ] && [ "$1" != "first" ]; then
  echo "Removing /Users/eusebiu.rizescu/dizertatie/flask/*"
  sudo rm -rf /Users/eusebiu.rizescu/dizertatie/flask/*
  echo "Removing /Users/eusebiu.rizescu/dizertatie/mysql-conf/*"
  sudo rm -rf /Users/eusebiu.rizescu/dizertatie/mysql-conf/*

  echo "Copying to /Users/eusebiu.rizescu/dizertatie/flask/*"
  sudo cp -R ./WebApplicationCode/* /Users/eusebiu.rizescu/dizertatie/flask/
  echo "Copying to /Users/eusebiu.rizescu/dizertatie/mysql-conf/*"
  sudo cp -R ./MySQL/* /Users/eusebiu.rizescu/dizertatie/mysql-conf/
fi


if [ "$1" != "stop" ]; then
  sleep 1
  sudo docker stack deploy -c docker-compose.yml webapplication
fi

if [ "$1" == "stop" ]; then
  # delete all containers
  echo "Delete all containers"
  sudo docker rm -f $(docker ps -a -q)
fi
