# Homework lesson_01

## Useful links:
 - Docker command line reference https://docs.docker.com/engine/reference/commandline/cli/
 - Dockerfile reference https://docs.docker.com/engine/reference/builder/
 - Passing Arguments to PHP script https://www.igorkromin.net/index.php/2017/12/07/how-to-pass-parameters-to-your-php-script-via-the-command-line/
 - Passing Argument to Node.js script https://nodejs.org/en/knowledge/command-line/how-to-parse-command-line-arguments/
 - How to keep Docker container running https://devopscube.com/keep-docker-container-running/
 - How to bind Host directory to Container directory https://docs.docker.com/storage/bind-mounts/ 

## Description

### Reading

Finish reading Dockerfile reference. 

Examples are available at official [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/) and [Exercise_04](./exercise_04_dockerfile/readme.md). 

Instructions that should be checked: COPY, ADD, VOLUME, USER, WORKDIR, STOPSIGNAL, ONBUILD, STOPSIGNAL, HEALTHCHECK

Reading about "Docker history <Container ID>" command. It is available at [Docker command line reference](https://docs.docker.com/engine/reference/commandline/cli/). It can be used to check commands that are run for specific images.

### Base Assignment

*Create your own Dockerfile

- Create a new Dockerfile
- Choose an image of your own choice from [DockerHub](https://hub.docker.com/search?type=image). It can be PHP, Node.js, Mysql or any other image. It is advised to use Official images. Use it as Base Image of your Dockerfile.
- Create a script of your own choice that can be executed from the container. It can be anything simple as "script.php", which would echo "Hello Docker!" to the console.
- Create a unit tests for your script. There should be one green (succesful) and one red (failed) unit test for your script. 
- COPY your script and unit test inside the Dockerfile
- Add entrypoint for your Dockerfile so that your script is executed when Docker Image is run
- Add information to the Dockerfile (example - Author). When Image is built it should be possible to use "Docker inspect" to accertain that you have built the specific image
- Create a public repository on [DockerHub](https://hub.docker.com/search?type=image) with name lesson_01_homework
- BUILD your image locally
- PUSH your image to [DockerHub](https://hub.docker.com/search?type=image). Image must be published with specific version "homework".
- Image must be available on Dockerhub with a specific tag. It should look something like <your username>/<your project name>:homework

### Bonus Assignments

*Adding additional functionality to your Dockerfile from Base Assignment*
 
 - Add a CMD argument that can be passed to your script. It can be something like "version", "greeting" or anything else. There are two example references for [PHP](https://www.igorkromin.net/index.php/2017/12/07/how-to-pass-parameters-to-your-php-script-via-the-command-line/) and [Node.js](https://nodejs.org/en/knowledge/command-line/how-to-parse-command-line-arguments/) on how to pass arguments to scripts.

*Create additional Healthcheck Dockerfile*
 
- Create a new Dockerfile. For separation, it can be named differently from the Dockerfile created for Base Assignment
- Choose an image of your own choice from [DockerHub](https://hub.docker.com/search?type=image). It can be PHP, Node.js, Mysql or any other image. It is advised to use Official images. Use it as Base Image of your Dockerfile.
- Add functionality with ENTRYPOINT, CMD or scripts so that the container runs indefinetly. 
- COPY your script inside the Dockerfile (Can be the same as in the Base Assignment)
- Add HEALTHCHECK to Dockerfile that would check the status of the running container every 5 seconds
- Add an environmental variable that would cause the HEALTHCHECK to fail if proviided different values. For example for value=0 healthcheck fails, for value=1 healthcheck succeeds.
- Add Volume to your image.
- Edit your script to save, modify or in any other way change data in your Volume. It should be possible to see how your Volume folder has added files or folders, when script is run.
- Create a public repository on [DockerHub](https://hub.docker.com/search?type=image) with name Lesson_01_homework_bonus
- BUILD your image locally
- PUSH your image to [DockerHub](https://hub.docker.com/search?type=image). Image must be published with specific version "homework_bonus".
- Image must be available on Dockerhub with a specific tag. It should look something like <your username>/<your project name>:homework_bonus
 
*Create additional Webserver Dockerfile* (hard)
 
Note: For easy of development, Directory binding can be used that bind host directory to container directory https://docs.docker.com/storage/bind-mounts/ 

- Create a new Dockerfile. For separation, it can be named differently from the Dockerfile created for Base Assignment or the First Bonus assignment
- Choose an image of your own choice from [DockerHub](https://hub.docker.com/search?type=image). It should be an image like [Node.js](https://hub.docker.com/_/node), [Nginx](https://hub.docker.com/_/nginx)+PHP or any other webserver with your desired programming language. You can create a webserver manually if desired.. It is advised to use Official images. Use it as Base Image of your Dockerfile.
- Add a number that can be used inside the webserver
- Create an endpoint GET "/increment" in the webserver that would increase the number and display it
- Create an endpoint GET "/decrement" in the webserver that would increase the number and display it
- Expose ports that are required for the server to be reachable from localhost:8081 or some different port localhost:XXXX
- COPY your code inside the Dockerfile to a specific directory so that webserver accesses the data and works, when building the image
- Create a public repository on [DockerHub](https://hub.docker.com/search?type=image) with name Lesson_01_homework_bonus_2.
- BUILD your image locally
- PUSH your image to [DockerHub](https://hub.docker.com/search?type=image). Image must be published with specific version "homework_bonus_2".
- Image must be available on Dockerhub with a specific tag. It should look something like <your username>/<your project name>:homework_bonus_2

