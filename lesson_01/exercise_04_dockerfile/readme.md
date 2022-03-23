# Dockerfile

Dockerfile Commands 

### FROM

Initializes a new build stage and sets the Base Image for subsequent instructions

Each Dockerfile must start with a FROM instruction. 

Base image can be any image from Container Repository

    FROM alpine:latest

### RUN

Runs a command while building the image. Command can be anything

    RUN mkdir - /logs && touch /logs/logs.txt
    RUN echo "Today is a good day!"
    
You can use \ (backslash) to continue a single RUN command onto the next line

    RUN echo "Hello" \
        echo "World!"
        
You can also use different shells if desired

    RUN ["sh", "-c", "echo 'Hello Docker!'"]
    
### CMD
CMD instructions is command parameter function. 

Dockerfile executes only the last CMD command, when Image is started
 
CMD has 3 forms:

First form is shell form. There the command is written in shell syntax 
  
    CMD command param1 param2
    CMD sh -c "echo 'Hello World'"

Second form is exec form similar to "Docker exec" command, where executable and its parameters is provided

    CMD ["executable","param1","param2"]
    CMD ["sh", "-c", "echo Hello Docker!"]
    
Third form is parameter form. In that case parameters are provided as arguments to ENTRYPOINT instruction
    
    CMD ["param1","param2"]
    CMD ["-c","Hello Docker!"]
    
Note: If Third form is provided. ENTRYPOINT command is also required as it is expected to pass the values as arguments 
to the ENTRYPOINT command.

### ENTRYPOINT

Entrypoint has the two forms which are similar to first two forms of CMD

First form is shell form. There the command is written in shell syntax 
  
    ENTRYPOINT command param1 param2
    ENTRYPOINT sh -c "echo 'Hello World'"

Second form is exec form similar to "Docker exec" command, where executable and its parameters is provided

    ENTRYPOINT ["executable","param1","param2"]
    ENTRYPOINT ["sh", "-c", "echo 'Hello Docker!'"]
    
### ENTRYPOINT + CMD

Entrypoint and CMD can be used together. Entrypoint can be set to stable default commands and arguments. 

CMD can have additional defaults set that are more likely to be changed.

    FROM ubuntu
    ENTRYPOINT ["sh", "-c"]
    CMD ["echo 'Hello World!'"]
    # When container is run this translates to 
    # sh -c "echo 'Hello World!'"
    
CMD command arguments can be changed, when running a container. ENTRYPOINT is executed the same way each time the container is run.

    docker run <Image> "echo 'Hello Docker!'"
    # It is equal to changing CMD parameter in Dockerfile
    ENTRYPOINT ["sh", "-c"]
    CMD ["echo 'Hello World!'"]
    # When container is run this translates to
    # sh -c "echo 'Hello Docker!'"
    

### LABEL

LABEL instruction adds metadata to an image. It can be checked when inspecting an image

    LABEL version="1.0"
    LABEL author="docker-student"

### EXPOSE

EXPOSE instructions informs the container to listen to network ports at runtime.
UDP and TCP ports can be enabled separately or together.

    EXPOSE 8080/udp
    EXPOSE 9000/tcp
    EXPOSE 9090

### ENV

ENV instruction sets the environmental variable to specified value. 

    ENV APP_NAME="exercise_04"
    ENV APP_AUTHOR="docker-student"

### ARG

ARG instructions sets argument values for building an image and they are only available at runtime. They can be passed build variables.

    ARG APP_VERSION="1.0"
    
### ARG + ENV

Sometimes there is a need to set specific variables when building images, but ARG variables do not persistent to runtime.
It can be solved by using ARG and ENV instructions together

    ARG ARG_APP_VERSION="1.0"
    
    ENV APP_VERSION=$ARG_APP_VERSION
    
After building an image with a specific ARG_APP_VERSION variable, the image will
have APP_VERSION environmental variable available on runtime.

### COPY

The COPY instruction copies files from host system <src> folder to Docker image <dest> folder
    
    COPY [--chown=<user>:<group>] <src>... <dest>
    COPY . /app/src/
    
In example All files and folders from .(dot) folder, which is equal to the current directory would be copied to the /app/src folder on the Docker image
    
### ADD

ADD instruction is similar to COPY command and mostly they work they same way. 
    
The difference is that ADD instruction can also handles tar files decompression and URLS. 
    
    ADD compressed.tar.gz /app/src/

### VOLUME

Volume instructions creates a mount point with a specified name and marks it as future mounted volume. 
It is then added as a volume on runtime.

    VOLUME ["/data"]
    
It can be used for defining storage for database volumes or other types of dynamic data. 
    
    

### USER

USER isntructions sets the user name (or UID) and optionally the user group (or GID) to use when executing build steps in Dockerfile

    USER application
    
###WORKDIR

Workdir sets the woroking directory for following commands.

    WORKDIR /app

### STOPSIGNAL

### ONBUILD

ONBUILD instruction is a prefix for any other instructions that can be used to add another build step to 
future images. 

For example if we have a webserver. We can add onbuild function to add files, when building. 

    # Webserver example with tag webserver:latest (fake example)
    FROM alpine:latest    
    ONBUILD ADD . /app/src

Even after extending the image and without specifying any other commands, the commands willl be run in the next build stages

    # New image
    FROM webserver:latest
    LABEL version="1.1"
    
After building the New image, the files from current directory will be copied to 
/app/src folder. 

### STOPSIGNAL
    
STOPSIGNAL instructions sends a system call signal that causes the container to exit

### HEALTHCHECK

Healthcheck instruction instructs the server to check the container for healthy status based on configuration
If healthcheck fails it write to console or error log.

    HEALTHCHECK --interval=5m --timeout=3s CMD curl -f http://localhost:8080/ || exit 1

