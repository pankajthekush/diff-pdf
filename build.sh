#!/bin/bash

# build the docker file and push

docker-compose build --no-cache
docker push pkumdev/diff-pdf