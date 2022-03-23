FROM alpine:latest

ARG ARG_APP_VERSION="2.0"

ENV APP_NAME="exercise_04"
ENV APP_AUTHOR="docker-student"
ENV APP_VERSION="1.0"

RUN mkdir - /logs && touch /logs/logs.txt

LABEL version="1.0"
LABEL author="docker-student"

# Run image infinitely, unless it is stopped
#ENTRYPOINT ["tail", "-f", "/dev/null"]

# Run image once. Just execute a specific command
ENTRYPOINT ["sh", "-c"]
CMD ["echo 'Hello Docker!'"]

EXPOSE 443
EXPOSE 8080/udp
EXPOSE 9000/tcp
EXPOSE 9090
EXPOSE 80



