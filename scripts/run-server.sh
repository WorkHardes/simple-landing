#!/bin/bash

set -eux

granian app:src.main --host=${SERVER_HOST} --port=${SERVER_PORT}
