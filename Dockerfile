FROM python:3.6

ADD requirements.txt .

RUN pip install -r requirements.txt

ADD . /src

WORKDIR /src

EXPOSE 80

CMD ["python", "web.py"]