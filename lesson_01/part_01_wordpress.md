### Start a mysql server

    docker run --name wordpress-mysql -e MYSQL_ROOT_PASSWORD="secret" -e MYSQL_USER=wordpress -e MYSQL_PASSWORD=wordpress -e MYSQL_DATABASE=wordpress -d mysql
    
    
### Start a wordpress server

    docker run --name wordpress-web -e WORDPRESS_DB_HOST=host.docker.internal -e WORDPRESS_DB_USER=root -e WORDPRESS_DB_PASSWORD=secret -e WORDPRESS_DB_NAME=wordpress -e WORDPRESS_DEBUG=1 -p 8080:80 -d wordpress