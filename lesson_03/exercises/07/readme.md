# Exercise 03

## Introduction

Adding a web server to docker-compose

### Description

You must spin up multiple Docker containers using `docker compose`, attention - you will need to write some code as well for web server and to connect to MQ & DB.

## App1 container

App1 starts a webserver on port 8080 and exposes an url http://localhost:8080/ping when this endpoint is called message is sent to the message queue running in the next container.

## Message-Queue container

Message Queue container runs in a container and is listening to messages, when message is received it updates a counter stored in the database that is running in the next container.

## Database container

Any type of the database with a single table where a counter is stored.

## App2 container

App2 starts a webserver on port 8081 and exposes an url http://localhost:8081/pong that displays counter value.

### Requirements for Completion

- All servers are working
