#!/usr/bin/env sh

# depending on whether we're running in development or in staging/production, we want to
# either execute the app (web) with the runserver or with uwsgi
# additionally we can trigger celery worker and beat execution
case "$DJANGO_RUN_ENV" in
  dev)    python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:80 ;;
  web)    python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:80 ;;
  worker) celery worker -l $CELERY_LOG_LEVEL -A buzzword_counter.configuration.celery.app --workdir /code/ --uid $CELERY_UID --gid $CELERY_GID -O fair ;;
  beat)   celery beat -l $CELERY_LOG_LEVEL -A buzzword_counter.configuration.celery.app --workdir /code/ --uid $CELERY_UID --gid $CELERY_GID --pidfile=/var/run/celery/celerybeat.pid --schedule /var/run/celery/celerybeat-schedule ;;
esac
