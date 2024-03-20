#!/bin/bash

set -eu

set -o allexport
source ./env_files/.env.dev set

granian --interface=asgi --host=${SERVER_HOST} --port=${SERVER_PORT} src.main:app
