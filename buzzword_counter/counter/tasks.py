import logging

from buzzword_counter.configuration.celery import app
from buzzword_counter.counter.models import Buzzword


@app.task
def add_buzzword(buzzword):
    Buzzword.objects.create(word=buzzword)
    logging.info(f'Created buzzword "{buzzword}"')
