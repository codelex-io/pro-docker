# Add the Dockerfile to the Docker-compose

## Add your own services to the docker-compose.yml

### Add Service with image option
    php:
        image: php:8
        
### Add Service with build option

    php_build:
        build: .

### Add Service with build option, context and arguments
  
    php_build_context:
        build:
            context: .
            dockerfile: Dockerfile
            args:
                author: "docker-student"