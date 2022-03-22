FROM alpine:latest

ARG ARG_APP_VERSION="2.0"

ENV APP_NAME="exercise_04"
ENV APP_AUTHOR="docker-student"
ENV APP_VERSION="1.0"

RUN mkdir - /logs && touch /logs/logs.txt
RUN echo "Today is a good day!"

LABEL version="1.0"
LABEL author="docker-student"

#CMD ["Hello World"]

#CMD ["powershell", "-c", "echo Hello Docker!"]


#ENTRYPOINT sh -c "echo"

#ENTRYPOINT ["top", "-b"]
#CMD ["-c"]

ENTRYPOINT ["tail", "-f", "/dev/null"]

EXPOSE 443
EXPOSE 8080/udp
EXPOSE 9000/tcp
EXPOSE 9090
EXPOSE 80
