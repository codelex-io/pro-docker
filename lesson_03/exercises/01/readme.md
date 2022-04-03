# Exercise 01

## Introduction

How to create a Docker Image and Docker Container

### Description
Create a Dockerfile with alpine:latest image as base image. 

Build the Dockerfile that was created. Add a tag: `exercise_01_image`

Run the image with a name: `exercise_01_container`

### Requirements for Completion

- Running command `docker images --filter=reference=exercise_01_image` lists the image `exercise_01_image`
- Running command `docker ps -a --filter "name=exercise_01_container"` lists the container `exercise_01_container`
- Running command `grep -q "alpine:latest" Dockerfile && echo "Success" || echo "Fail"` should display text `Success`

