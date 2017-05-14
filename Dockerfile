FROM python:3.4-alpine

ADD ./script /script

WORKDIR /script

RUN pip install -r requirements.txt

CMD ["python", "-u", "app.py"]
