# Example of a Web server

A group of commands to create a working Wordpress server.

Try to execute the commands one after another

### Create a local network

    docker network create --driver bridge wordpress_network

### Start a mysql server

    docker run --name wordpress_mysql --network wordpress_network -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_USER=wordpress -e MYSQL_PASSWORD=wordpress -e MYSQL_DATABASE=wordpress -e MYSQL_ROOT_HOST=% -p 3306:3306 -d mysql
    
    
### Start a wordpress server

    docker run --name wordpress_web --network wordpress_network -e WORDPRESS_DB_HOST=wordpress_mysql -e WORDPRESS_DB_USER=wordpress -e WORDPRESS_DB_PASSWORD=wordpress -e WORDPRESS_DB_NAME=wordpress -e WORDPRESS_DEBUG=1 -p 8080:80 -d wordpress
    
### Visit the website

Visit http://localhost:8080 to view your wordpress website
