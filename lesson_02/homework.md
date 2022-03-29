# Homework lesson_02

## Description

### Reading

Re-read about Dockerfile and Docker-Compose. 

There will be a quiz

### Base Assignment

Add the Docker Image that was created in #Base Assignment of lesson_01 to docker-compose. 

It should fill the following criteria:

1. Service should be created with a name "base_homework" that has an image of the "base_homework" from 
the lesson_01_homework. It should use a work ready image. 
Image name should be "<your_dockerhub_user>/<project_name>:homework".
2. Service should be created with a name "base_homework_tests" that has an image of the "base_homework" from
the lesson_01_homework. It should use a work ready image. 
Image name should be "<your_dockerhub_user>/<project_name>:homework".
3. Service "base_homework" should run "script" that is defined in #Base Assignment of 
lesson_01 homework, when it is started.
4. Service "base_homework_tests" should run "unit test" that is defined in #Base Assignment
of lesson_01 homework, when it is started.

### Bonus Assignments

Add the Docker Images that was created in #Bonus Assignments of lesson_01 to docker-compose

It should fill the following criteria:

1. Service should be created with a name "bonus_homework" that has an image of the "bonus_homework" from 
the lesson_01_homework. It should use a work ready image. 
Image name should be "<your_dockerhub_user>/<project_name>:homework_bonus".
2. Service should be created with a name "bonus_homework_second" that has an image of the "bonus_homework_2" from
the lesson_01_homework. It should use a work ready image. 
Image name should be "<your_dockerhub_user>/<project_name>:homework_bonus_2".
3. Service "bonus_homework" should have HealthCheck
4. Service "bonus_homework" should have a Volume to store changed data by the script.
5. Service "bonus_homework" should have a Mounted Volume with Script directory mounted
both on the host and on the container. It should make it possible to modify script on runtime.
6. Service "bonus_homework_second" should have needed ports exposed so that the webserver
is accesible



