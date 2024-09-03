FROM python

WORKDIR /src

ENV PYTHONUNBUFFERD 1
ENV TZ='Asia/Tehran'
COPY requirement.txt .

RUN apt-get update && apt-get install -y wget gnupg
RUN wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -

RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*
    
RUN pip install -r requirement.txt
COPY wait-for-it.sh /wait-for-it.sh

COPY . .


EXPOSE 8000
