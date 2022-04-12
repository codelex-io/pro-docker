# Exercise 04

## Introduction

How to work with networking in Docker

### Description

Create multiple services of any kind in your docker compose and add them to different networks and different drivers.

Example of adding 2 different networks:
https://medium.com/@caysever/docker-compose-network-b86e424fad82

Network and network driver documentation:
https://docs.docker.com/network/

### Requirements for Completion

- 2 networks without a specified driver (similar or exact as in the example link) with at least 1 container assigned to the network
- 1 network with "host" driver with at least 1 container assigned to the network
- 1 network with "none" driver with at least 1 container assigned to the network

### Explanation

Sometimes we need to couple containers together in a single network. Sometimes we need to completely isolate a container from other containers due to security concerns. 

By default "docker-compose" creates its own network (bridge driver), when setting up the environment (docker compose up).

Additional information:

https://www.docker.com/blog/understanding-docker-networking-drivers-use-cases/

