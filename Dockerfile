FROM python:3.10

WORKDIR /usr/src/films
ADD . /usr/src/films

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /usr/src/films/docker-entrypoint.sh

ENTRYPOINT ["/usr/src/films/docker-entrypoint.sh"]