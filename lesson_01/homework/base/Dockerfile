# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
ENV AUTHOR="Valdis A."
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install flask redis pytest
EXPOSE 5000
COPY . .
CMD ["flask", "run"]