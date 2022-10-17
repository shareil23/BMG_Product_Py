FROM python:3.7-slim as base


### Stage BUILD ###
FROM base as builder

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat \
    libpq-dev \
    gcc

COPY ./requirements.txt /requirements.txt

RUN pip3 install --upgrade pip && \
    pip3 install --upgrade setuptools wheel && \
    pip3 install -r requirements.txt


### Stage Runner ###
FROM base as runner

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y netcat \
    libpq-dev \
    gcc

COPY --from=builder /usr/local/bin /usr/local/bin
COPY --from=builder /usr/local/lib /usr/local/lib

EXPOSE 5000
WORKDIR /service

COPY . /service/