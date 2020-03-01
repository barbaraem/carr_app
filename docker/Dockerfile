FROM python:3.7.3-slim-stretch
ENV PYTHONUNBUFFERED 1
ENV VIRTUAL_ENV /project/vendor
ENV PROJECT_DIR /project/app
ENV PATH $VIRTUAL_ENV/bin:$PATH
ENV PIP_CACHE_DIR $VIRTUAL_ENV/cache/
ENV PIPENV_CACHE_DIR $PIP_CACHE_DIR
ENV PYTHONPATH $PYTHONPATH:$PROJECT_DIR/src
ENV MYPYPATH $PYTHONPATH:$PROJECT_DIR/src

RUN apt-get update \
    && apt-get install -y --no-install-recommends apt-utils\
        libxml2 \
        libpq5 \
        gdal-bin \
        libcairo2-dev \
        libcogl-pango-dev \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/cache/apk/*

RUN addgroup --system --gid 101 django \
    && useradd -g django django \
    && mkdir -p /project/media /project/static $VIRTUAL_ENV

WORKDIR $PROJECT_DIR

ADD requirements.txt $PROJECT_DIR/

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

COPY . $PROJECT_DIR

RUN chown -R django: /project

USER django

# Can't use PROJECT_DIR env var in exec ENTRYPOINT
ENTRYPOINT ["/project/app/docker/entrypoint.sh"]
CMD ["uwsgi"]
EXPOSE 8000
