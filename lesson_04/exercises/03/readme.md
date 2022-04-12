# Exercise 03

## Introduction

How to work with a container locally (folder mount)

### Description

Create a web server (your own choice) with one endpoint that displays anything. Logic can be taken from previous exercises. 
All web server related files should be available in the exercise_01 folder

Modify docker compose and add a volume mount for the whole exercise_01 folder to the proper folder inside the server so that
the web server would still be fully functional

Example for volume: [volume-usage-example](https://medium.com/@chandrajeetmaurya/docker-compose-setting-up-web-development-stack-step-by-step-81e557a69863#:~:text=that%20its%20working.-,Volumes,-In%20ideal%20web)

### Requirements for Completion

- Modify anything on the webserver locally so that it would be represented as changes on the server.
Example: If you have an endpoint that displays "Hello Docker!". Change "Hello Docker!" to "Hello Exercise 01!" in local files.
After only changing the text, the endpoint response should be changed instantly to "Hello Exercise 01!". 

### Explanation

When working we do not want to wait for a long time until our server rebuilds to view our changes. So we mount a folder
from host to Docker container to see the changes instantly.