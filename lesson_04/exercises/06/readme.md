# Exercise 06

## Introduction

How to use Docker-compose profiles

### Description

First read [Docker compose profiles documentation](https://docs.docker.com/compose/profiles/)

Then add a web server of your own choice and a database server to docker-compose.

Add a test script that could be executed as an alternative entry-point or create a different test image. Add test script to docker-compose. as a separate server.

Create multiple profiles for the current configuration:
 - all - starts all the services
 - server - starts only the web server
 - tests - starts only the tests
 - database - starts only the database 
 - server_with_tests - starts web server + tests


### Requirements for Completion

 - Have 3 different servcies in docker-compose.yml - web server, test server, database server
 - Have 5 different profiles in docker-compose.yml - all, server, tests, database, server_with_tests
 - All profiles are working and it is possible to execute each of them. 

### Explanation

Sometimes there is a need to only run part of the servers you have in the configuration. 

For example: 
 - before release, you can run the tests container
 - when there is a remote database, you can run just the server or server_with_tests profile
