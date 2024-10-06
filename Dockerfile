FROM python:alpine3.20

WORKDIR /P5Software/FireFly-Configurator

ADD main.py .
ADD requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "./main.py"] 