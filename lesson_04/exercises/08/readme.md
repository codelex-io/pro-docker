# Exercise 07

## Introduction

How to split your application into blocks?

### Description

Investigate the `docker-compose.example.yml` file. It comes from [Dockerized Laravel github example](https://github.com/aschmelyun/docker-compose-laravel). 
Check how services are split into different containers.

Take your web server from your previous exercises and split it into several services.


### Requirements for Completion

- succesfully split your web server into several servers thus breaking down your application into multiple components

### Explanation

In the production environments your PHP will not need `composer` or `npm` services. They are only needed to install the
needed files and configurations. They can be separated into separate services that would only be used once or twice.