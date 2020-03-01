#!/bin/sh
set -e

MANAGE_CMD='python src/manage.py'

if [ "$1" = 'manage' ]; then
    shift
    exec ${MANAGE_CMD} $@
elif [ "$1" = 'runserver' ]; then
    shift
    exec ${MANAGE_CMD} runserver 0.0.0.0:8000 $@
elif [ "$1" = 'uwsgi' ]; then
    shift
    exec uwsgi --ini=/project/app/docker/uwsgi.ini $@
elif [ "$1" = 'celery' ]; then
    shift
    exec celery -A config worker $@
elif [ "$1" = 'beat' ]; then
    shift
    exec celery -A config beat $@
elif [ "$1" = 'test' ]; then
    shift
    exec pytest $@
elif [ "$1" = 'lint' ]; then
    shift
    OPTS=${@:-'.'}
    echo "-- black --" && black --check --diff $OPTS || EXIT=$?
    echo "-- isort --" && isort -c -rc --diff $OPTS || EXIT=$?
    echo "-- flake8 --" && flake8 $OPTS || EXIT=$?
    MYPY_OPTS=${@:-'src/'}
    echo "-- mypy --" && mypy $MYPY_OPTS || EXIT=$?
    exit ${EXIT:-0}
elif [ "$1" = 'fmt' ]; then
    shift
    OPTS=${@:-'.'}
    echo "-- black --" && black $OPTS
    echo "-- isort --" && isort -rc -ac $OPTS
    exit 0
fi

exec "$@"
