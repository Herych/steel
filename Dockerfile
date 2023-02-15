FROM python:3.8

WORKDIR /src
COPY requirements.txt /src

RUN pip install --upgrade pip

RUN pip install -r requirements.txt
COPY . /src

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]
