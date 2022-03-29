# Docker-compose commands

## Reference

https://docs.docker.com/compose/reference/

## Docker compose commands

Most used docker compose commands

### Detached option

    docker compose <command> -d

### Starting

Starts existing containers. Fails if there are no existing containers

    docker compose start  

### Stopping
    
Stops existing containers. Fails if there are no existing containers
    
    docker compose stop

### Killing

Stops and removes the containers

    docker compose kill

### Up (Create + Start)

Starts and Creates if the contaienrs do not exist

    docker compose up

### Down (Stop + Remove)

Stops the Docker contains and Removs them

    docker compose down

### Restart

    docker compose restart

### Build

    docker compose build
