#!/usr/bin/bash

CONTAINER_NAME="some_generic_sm_app"
DOCKER_FILE="docker-compose.yml"

docker-compose stop
docker-compose -f ${DOCKER_FILE} rm --force
docker-compose -f ${DOCKER_FILE} build
docker-compose -f ${DOCKER_FILE} up -d --remove-orphans
docker exec -it ${CONTAINER_NAME} /bin/bash

