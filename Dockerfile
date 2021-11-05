FROM quay.io/blueshoe/python3.9-slim
ENV PYTHONUNBUFFERED 1

RUN apt update \
    && apt install -y libpq-dev gcc python3-dev mime-support gettext libgettextpo-dev
RUN /usr/local/bin/python -m pip install --upgrade pip
COPY requirements.txt /usr/src/
RUN pip3 install -r /usr/src/requirements.txt \
    && apt purge -y gcc python3-dev \
    && apt autoremove -y --purge

RUN mkdir /code
WORKDIR /code

COPY . /code/


# we should have an unprivileged user to run celery
# we need a directory for celery uid/gid to store celerybeat pidfile and schedule
RUN groupadd --gid 1337 bs \
    && useradd --create-home --uid 1337 --gid 1337 --shell /bin/bash bs \
    && mkdir /run/celery/ && chown 1337:1337 /run/celery/
