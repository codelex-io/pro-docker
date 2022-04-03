# Exercise 02

## Introduction

How to make a container run indefinitely

### Description

Copy Dockerfile from Exercise 01.
Modify Dockerfile by adding an indefinitely running command as entry-point of the image. Additionally install `GIT` on 
the image.

Build the Dockerfile that was created. Add a tag: `exercise_02_image`
Run a new container with a name: `exercise_02_container`

Execute `git --version` inside the running container to check if it is installed correctly

### Requirements for Completion

- `docker ps` command displays the container `exercise_02_container` as running.
- `git --version` command displays git version, when executed inside the container `exercise_02_container`
