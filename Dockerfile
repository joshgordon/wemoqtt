FROM python:3

RUN mkdir -p /app
WORKDIR /app

ADD script.py .
ADD requirements.txt .

RUN pip install -r requirements.txt
CMD python script.py
