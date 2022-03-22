# Building and publishing an image

## Creating an account on Dockerhub

https://hub.docker.com/signup

## Docker login

Run docker login command and authenticate with your credentials to Dockerhub

    Docker login
    
## Docker build

Build an image that you can upload to the Dockerhub

    Docker build -t <username>/<project-name>:<tag> .
    Docker build -t docker-course/pro-docker:latest .
    
## Docker push

Push a built image to Dockerhub

    Docker push <username>/<project-name>:<tag>
    Docker push docker-course/pro-docker:latest
    
