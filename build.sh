#!/bin/bash

# Load environment variables from .env file
if [ -f .env ]; then
  export $(cat .env | xargs)
fi

# Define your Docker image name and tag
IMAGE_NAME="cogniezer"
IMAGE_TAG="latest"

# Build the Docker image with build arguments
docker build \
  --build-arg AZURE_KEY=${AZURE_KEY} \
  --build-arg AZURE_REGION=${AZURE_REGION} \
  --build-arg HOST=${HOST} \
  --build-arg PORT=${PORT} \
  -t ${IMAGE_NAME}:${IMAGE_TAG} \
  --progress=plain .

# Optionally, remove the environment variables after the build
unset AZURE_KEY
unset AZURE_REGION
unset HOST
unset PORT