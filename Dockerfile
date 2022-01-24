FROM python:3.9-buster

RUN apt-get update && \
    apt-get install -y cron

COPY ./cronjob /etc/cron.d/cronjob
RUN chmod 0644 /etc/cron.d/cronjob
RUN crontab /etc/cron.d/cronjob
RUN service cron start

COPY ./requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt

ADD . /app
WORKDIR /app

CMD python /app/tinynews.py receive
