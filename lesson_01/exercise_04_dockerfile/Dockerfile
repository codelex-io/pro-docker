FROM alpine:latest

ARG ARG_APP_VERSION="1.0"

LABEL version="1.0"
LABEL author="docker-student"

ENV APP_NAME="exercise_04"
ENV APP_AUTHOR="docker-student"
ENV APP_VERSION=$ARG_APP_VERSIOn

VOLUME ["/data"]

USER application

WORKDIR /app

RUN mkdir - /logs && touch /logs/logs.txt
RUN echo "Today is a good day!"

RUN echo "Hello" \
    echo "World!"

RUN ["/bin/bash", "-c", "echo 'Hello Docker!'"]

ENTRYPOINT ["/bin/bash", "-c", "echo"]

CMD ["Hello World"]

EXPOSE 8080/udp
EXPOSE 9000/tcp
EXPOSE 9090