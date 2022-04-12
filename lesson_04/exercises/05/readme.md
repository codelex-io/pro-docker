# Exercise 05

## Introduction

How to change environmental variables within Docker compose

### Description

First read [Docker compose environmental variables documentation](https://docs.docker.com/compose/environment-variables/)

Create a web server that uses environmental variables in any way in the constraints of docker-compose.

You can add a dynamic port that could be changed from the env file. 

Add a different env file `.env.test`. Add different data in the file

### Requirements for Completion

- have an existing .env file
- have atleast 3 environmental variables used in docker-compose.yml file
- have all environmental variables used in docker-compose.yml file defined in .env file
- have an existing .env.test file
- .env file should differ from .env.test file
- `docker-compose --env-file .env.test up` works and provides different results from `docker-compose up`

### Explanation

Often Docker-compose has servers that need to communicate between them. An example would be a web server, a database and a cache server.
There can also sometimes be port conflicts as we have had in previous lessons (80 or 8080). 
To make it more dynamic - environmental variables are used. They can define passwords through multiple servers and ports can also be defined in the .env file. 

