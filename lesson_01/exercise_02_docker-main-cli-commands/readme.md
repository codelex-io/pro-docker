# Docker main CLI commands

### Docker version

Retrieve docker version information

    Docker --version
    
### Docker pull

Downloads an image from container repository. Mostly https://hub.docker.com/

    docker pull <Image:Image version>
    docker pull mysql
    docker pull mysql:8
    
When pulling it is not required to specify a version. If not specified "latest" tag is downloaded.
    
### Docker run

Runs a specified image

    docker run -d <Image>
    docker run -d mysql:8
    
### Docker ps

Lists containers that exist in the working environment

    docker ps
    
By default the command shows only running containers. To show also stopped containers, you cann add -a option

    docker ps -a
    
### Docker exec

Runs a new command in a running container

    docker exec -it <CONTAINER ID> bash
    docker exec -it wordpress_mysql sh -c "echo Hello Docker"
    
Exec command can also be used to launch an interactive console inside the container

    docker exec -it <CONTAINER ID> bash
    docker exec -it wordpress_mysql bash
    
To exit from the interactive console press ***Ctrl + c*** or type ***exit***

option *-it* is needed to make the command run interactively and within a terminal.
Interactivity is needed to listen from the responses from the container and 
Terminal is needed for displaying and inputing the information visually.

### Docker stop

Stops a running container

    docker stop <CONTAINER ID>
    docker stop wordpress_mysql
    
### Docker start

Starts a stopped container

    docker start <CONTAINER ID>
    docker start wordpress_mysql
    
### Docker kill

Kills a running container immediately. 

    docker kill <CONTAINER ID>
    docker kill wordpress_mysql

Docker kill is similar to Docker stop command. The difference is that the kill command kills the container instantly,
while Docker stop sends a STOP signal to the container and wait's for it to shutdown itself.

Kill command can be used in cases, when you think your container is stuck
    
### Docker images

Lists locally available docker images

    docker images
    
### Docker rm
   
Deletes a stopped container

    docker rm <CONTAINER ID>
    docker rm wordpress_mysql
   
Stopped containers still retain all the environmental variables and configuration they were started with.

To remove an existing container, so that a new container can be started in its place, the rm command can be used.

### Docker build

Builds an image from a specified Dockerfile

    docker build .
    
By default build command looks for file with name "Dockerfile".
It can be changed with option "-f"

    docker build . -f exercise_02/Dockerfile
    
### Docker inspect

Shows information about image

    docker inspect <Image>
    
It helps to check the information of an image if needed. It provides useful information like set environmental
variables, Container config, Command to be run at start, Volumes, Ports etc

### Docker rmi

Removed a specific image from local repository

    docker rmi <CONTAINER_ID>
    
### Docker history

See history of a Docker image. It shows the instructions that Docker image executes from last to first instruction in ascending order.

    docker history mysql:8

### Docker login

Logins to a container repository. Requires an account in the specific repository.  

    docker login 

### Docker push

Pushes an image to the container repository, where you logged in. Requires logged in user.

    docker push <IMAGE>
    






