#!/bin/bash

set -eu

if [ ${#} -eq 0 ]
then
    echo "Write to first argument dev or prod"
    exit 1
fi


case ${1} in
    dev)
        docker_compose_file="docker-compose.dev.yaml"
        env_file=".env.dev"
    ;;
    prod)
        docker_compose_file="docker-compose.prod.yaml"
        env_file=.env
    ;;
    *)
        echo "Script parameter can be only dev, prod or test"
        exit 1
    ;;
esac

env_file_path="${PWD}/env_files/$env_file"
docker_compose_file_path="${PWD}/docker/${docker_compose_file}"
echo "docker compose file: ${docker_compose_file_path}"
echo "env file: ${env_file_path}"

set -o allexport
source ${env_file_path} set

docker compose --file $docker_compose_file_path down --remove-orphans --volumes || { echo 'docker compose down failed' ; exit 1; }
docker compose --file $docker_compose_file_path up --build -d || { echo 'docker compose up failed' ; exit 1; }
