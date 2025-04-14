# https://www.youtube.com/watch?v=0eMU23VyzR8

FROM python:3.9-buster

WORKDIR /app

COPY . /app

RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "--bind", "0:0:0:0:5000", "app:app"]