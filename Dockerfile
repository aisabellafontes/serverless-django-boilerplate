FROM python:3.6.5

ENV DB_USER 'admin'
ENV DB_PASSWORD 'boilerplate'
ENV DB_HOST 'serverless-django-boilerplate-db'
ENV DB_PORT 5432

RUN mkdir /code
WORKDIR /code

ADD requirements.txt /code/
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /code/

RUN chmod +x /code/start.sh
