FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1

# TODO: comment back once somewhat stable
#COPY requirements.txt /usr/src/
#RUN apt update \
#    && apt install -y libpq-dev gcc python3-dev mime-support gettext libgettextpo-dev \
#    && pip install -r /usr/src/requirements.txt \
#    && apt purge -y gcc python3-dev \
#    && apt autoremove -y --purge

RUN apt update \
    && apt install -y libpq-dev gcc python3-dev mime-support gettext libgettextpo-dev
COPY requirements.txt /usr/src/
RUN pip install -r /usr/src/requirements.txt \
    && apt purge -y gcc python3-dev \
    && apt autoremove -y --purge

RUN mkdir /code
WORKDIR /code

COPY . /code/

EXPOSE 8080

# we should have an unprivileged user to run celery
# we need a directory for celery uid/gid to store celerybeat pidfile and schedule
RUN groupadd --gid 1337 bs \
    && useradd --create-home --uid 1337 --gid 1337 --shell /bin/bash bs \
    && mkdir /run/celery/ && chown 1337:1337 /run/celery/

COPY deployment/run_app.sh /usr/src/run_app.sh
RUN chmod +x /usr/src/run_app.sh
CMD /usr/src/run_app.sh
