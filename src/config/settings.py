import logging
from datetime import timedelta

from django.core.exceptions import ImproperlyConfigured

import environ
import sentry_sdk
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration
from sentry_sdk.integrations.logging import LoggingIntegration


env = environ.Env()
root = environ.Path(__file__) - 2

BASE_DIR = root()
DEBUG = env("DEBUG", default=False)
SECRET_KEY = env("SECRET_KEY")
ALLOWED_HOSTS = env.list("ALLOWED_HOSTS", default=[])
SITE_ID = env("SITE_ID", default=1)
ROOT_URLCONF = "config.urls"
WSGI_APPLICATION = "config.wsgi.application"

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.sites",
    "django.contrib.staticfiles",
    "rest_framework",
    "config",
    "example_app",
)

MIDDLEWARE = (
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
)

# --- ADMIN ---
LOGIN_REDIRECT_URL = "/admin/"

# --- STATIC FILES ---
STATIC_URL = "/static/"
STATIC_ROOT = env("STATIC_ROOT", default="/project/static")
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
)

MEDIA_URL = "/media/"
MEDIA_ROOT = env("MEDIA_ROOT", default="/project/media")
#
# AWS_STORAGE_BUCKET_NAME = env("AWS_STORAGE_BUCKET_NAME", default=None)
# if AWS_STORAGE_BUCKET_NAME is not None:
#     INSTALLED_APPS += ("storages",)
#     DEFAULT_FILE_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
#     STATICFILES_STORAGE = "storages.backends.s3boto3.S3Boto3Storage"
#     AWS_ACCESS_KEY_ID = env("AWS_ACCESS_KEY_ID", default=None)
#     AWS_SECRET_ACCESS_KEY = env("AWS_SECRET_ACCESS_KEY", default=None)
#     AWS_S3_REGION_NAME = env("AWS_S3_REGION_NAME", default="eu-west-1")
#     S3_USE_SIGV4 = True
#     AWS_QUERYSTRING_AUTH = False

# --- TEMPLATES ---
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [root("templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": (
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.template.context_processors.media",
                "django.template.context_processors.request",
                "django.template.context_processors.static",
                "django.template.context_processors.tz",
            )
        },
    }
]

# --- REST FRAMEWORK ---
REST_FRAMEWORK = {
    "DEFAULT_PERMISSION_CLASSES": ("rest_framework.permissions.IsAuthenticated",),
    "DEFAULT_AUTHENTICATION_CLASSES": (
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ),
    "DEFAULT_RENDERER_CLASSES": ("rest_framework.renderers.JSONRenderer",),
    "NON_FIELD_ERRORS_KEY": "errors",
}


# --- AUTH ---
SIMPLE_JWT = {
    "AUTH_HEADER_TYPES": ("JWT",),
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=30),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),
}


AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# --- DEBUG TOOLBAR ---
ENABLE_DEBUG_TOOLBAR = env.bool("ENABLE_DEBUG_TOOLBAR", default=DEBUG)
if ENABLE_DEBUG_TOOLBAR:
    INSTALLED_APPS += ("debug_toolbar",)
    MIDDLEWARE += ("debug_toolbar.middleware.DebugToolbarMiddleware",)

    INTERNAL_IPS = ("172.18.0.1", "127.0.0.1", "localhost")
    DEBUG_TOOLBAR_CONFIG = {
        "INTERCEPT_REDIRECTS": False,
        "SHOW_TOOLBAR_CALLBACK": lambda *x: True,
    }

# --- CORS ---
CORS_ORIGIN_ALLOW_ALL = env.bool("CORS_ALLOW_ALL", default=False)
CORS_ORIGIN_WHITELIST = env.list("CORS_ORIGIN_WHITELIST", default=[])

# --- TIMEZONE ---
USE_TZ = True
TIME_ZONE = "UTC"

# --- LANGUAGES ---
USE_I18N = True
USE_L10N = True
LANGUAGE_CODE = "en-us"

# LANGUAGES = (
#     ("en", _("English")),
#     ("pl", _("Polish")),
# )
LOCALE_PATHS = (root("locale"),)

# --- FILE UPLOAD ---
FILE_UPLOAD_MAX_MEMORY_SIZE = 2_621_440  # i.e. 2.5 MB
FILE_UPLOAD_PERMISSIONS = None
FILE_UPLOAD_DIRECTORY_PERMISSIONS = None

# --- DATABASE ---
DATABASES = {
    "default": env.db(default="postgres://postgres:postgres@postgres:5432/postgres")
}


# --- CELERY ---
CELERY_BROKER_URL = env("CELERY_BROKER_URL", default="redis://redis:6379/2")
CELERY_RESULT_BACKEND = env("CELERY_RESULT_BACKEND", default="redis://redis:6379/3")
CELERY_DEFAULT_QUEUE = env("CELERY_DEFAULT_QUEUE", default="default")
CELERY_BEAT_SCHEDULE = {}

# --- CACHE ---
CACHES = {
    "default": env.cache(
        default="redis://redis:6379/1?client_class=django_redis.client.DefaultClient"
    )
}
