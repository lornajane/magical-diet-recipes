FROM alpine:3.11

RUN apk add --no-cache python3 postgresql-dev gcc python3-dev musl-dev \
&& pip3 install --upgrade pip \
&& pip3 install flask psycopg2-binary flask-bootstrap

COPY . /app

ENV FLASK_APP=/app/hello.py
CMD python3 -m flask run --host 0.0.0.0

EXPOSE 5000
