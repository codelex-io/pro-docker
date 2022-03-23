##Useful links:
 - Docker command line reference https://docs.docker.com/engine/reference/commandline/cli/
 - Dockerfile reference https://docs.docker.com/engine/reference/builder/
 - Passing Arguments to PHP script https://www.igorkromin.net/index.php/2017/12/07/how-to-pass-parameters-to-your-php-script-via-the-command-line/
 - Passing Argument to Node.js script https://nodejs.org/en/knowledge/command-line/how-to-parse-command-line-arguments/

## Description

### Finish reading Dockerfile reference

Finish reading Dockerfile reference. 

Examples are available at official [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/) and [Exercise_04](./exercise_04_dockerfile/readme.md). 

Instructions that should be checked: COPY, ADD, VOLUME, USER, WORKDIR, STOPSIGNAL, ONBUILD, STOPSIGNAL, HEALTHCHECK

### Base Assignment

Creating your own Dockerfile

- Choose an image of your own choice from [DockerHub](https://hub.docker.com/search?type=image). It can be PHP, Node.js, Mysql or any other image. It is advised to use Official images. Use it as Base Image of your Dockerfile.
- Create a script of your own choice that can be executed from the container. It can be anything simple as "script.php", which would echo "Hello Docker!" to the console.
- COPY your script inside the Dockerfile
- Add entrypoint for your Dockerfile so that your script is executed when Docker Image is run
- Add a CMD argument that can be passed to your script. It can be something like "version", "greeting" or anything else. There are two example references for [PHP](https://www.igorkromin.net/index.php/2017/12/07/how-to-pass-parameters-to-your-php-script-via-the-command-line/) and [Node.js](https://nodejs.org/en/knowledge/command-line/how-to-parse-command-line-arguments/) on how to pass arguments to scripts. 
- Add information to the Dockerfile (example - Author). When Image is built it should be possible to use "Docker inspect" to accertain that you have built the specific image
- BUILD your image locally
- PUSH your image to [DockerHub](https://hub.docker.com/search?type=image). Image must be published with specific version "lesson_01_homework".
- Image must be available on Dockerhub with a specific tag. It should look something like <your username>/<your project name>:lesson_01_homework
 

### Bonus Assigment



