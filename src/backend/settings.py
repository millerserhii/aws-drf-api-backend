import os
from pathlib import Path
from typing import Any

import django
from configurations import Configuration, values
from django.utils.encoding import force_str

from utils.logger_settings import get_logger_settings


class Base(Configuration):

    django.utils.encoding.force_text = force_str

    # Build paths inside the project like this: BASE_DIR / 'subdir'.
    BASE_DIR = Path(__file__).resolve().parent.parent
    env_file = (BASE_DIR / "../.env").resolve()
    DOTENV = env_file if env_file.is_file() else None

    DEBUG = values.BooleanValue(True)

    # Logging Configuration
    LOGS_DIR = Path(f"{BASE_DIR}/logs")
    if not LOGS_DIR.exists():
        LOGS_DIR.mkdir()

    LOGGING = get_logger_settings(LOGS_DIR, DEBUG)

    SECRET_KEY = values.Value("django-insecure-only-for-development")

    ALLOWED_HOSTS = values.ListValue([".localhost", "127.0.0.1", "[::1]"])

    FRONTEND_URL = values.Value("http://localhost:5173")

    CORS_ALLOWED_ORIGINS = values.ListValue(
        ["http://localhost:5173", "http://127.0.0.1:5173"]
    )
    CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS
    CORS_ALLOW_CREDENTIALS = True

    SECURE_SSL_REDIRECT = values.BooleanValue(False)

    ROOT_URLCONF = "backend.urls"
    WSGI_APPLICATION = "backend.wsgi.application"
    CSRF_COOKIE_SECURE = True
    LANGUAGE_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
    DEFAULT_PAGE_SIZE = 100
    SIMPLE_HISTORY_FILEFIELD_TO_CHARFIELD = True

    LANGUAGE_CODE = "en-US"
    TIME_ZONE = "UTC"
    USE_I18N = True
    USE_TZ = True
    LOCALE_PATHS = ["locale"]

    STATIC_URL = "/static/"
    STATIC_ROOT = values.PathValue(BASE_DIR / "../static", check_exists=False)
    MEDIA_URL = "/media/"
    MEDIA_ROOT = values.PathValue(BASE_DIR / "../media", check_exists=False)
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.InMemoryStorage",
        },
        "staticfiles": {
            "BACKEND": (
                "whitenoise.storage.CompressedManifestStaticFilesStorage"
            ),
        },
    }

    EMAIL = values.EmailURLValue("console://")
    EMAIL_USE_LOCALTIME = True
    DEFAULT_FROM_EMAIL = "Versus Network"
    SERVER_EMAIL = "Versus Network"
    ADMINS = [
        ("Sergej Müller", "millerserhii@gmail.com"),
    ]

    # Application definition

    INSTALLED_APPS = [
        "django.contrib.admin",
        "django.contrib.auth",
        "django.contrib.contenttypes",
        "django.contrib.sessions",
        "django.contrib.messages",
        "django.contrib.staticfiles",
        "django.contrib.sites",
        # third party
        "rest_framework",
        "rest_framework.authtoken",
        "drf_spectacular",
        "corsheaders",
        "djoser",
        "django_filters",
        "simple_history",
        "django_redis",
        "health_check",
        "health_check.cache",
        "health_check.contrib.migrations",
        "health_check.contrib.psutil",
        "health_check.db",
        "health_check.storage",
        # apps
    ]

    MIDDLEWARE = [
        "kolo.middleware.KoloMiddleware",
        "django.middleware.security.SecurityMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        "simple_history.middleware.HistoryRequestMiddleware",
        "backend.middleware.request_log.RequestLogMiddleware",
        "backend.middleware.thread_local.ThreadLocalMiddleware",
    ]

    AUTHENTICATION_BACKENDS = [
        "django.contrib.auth.backends.ModelBackend",
    ]

    ROOT_URLCONF = "backend.urls"

    REST_FRAMEWORK = {
        "DEFAULT_AUTHENTICATION_CLASSES": (
            "rest_framework.authentication.TokenAuthentication",
            "rest_framework_simplejwt.authentication.JWTAuthentication",
        ),
        "DEFAULT_PERMISSION_CLASSES": [
            "rest_framework.permissions.DjangoModelPermissions",
        ],
        "DEFAULT_PAGINATION_CLASS": (
            "rest_framework.pagination.PageNumberPagination"
        ),
        "PAGE_SIZE": 50,
        "DEFAULT_FILTER_BACKENDS": [
            "django_filters.rest_framework.DjangoFilterBackend"
        ],
        "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    }

    SPECTACULAR_SETTINGS = {
        "TITLE": "Backend API",
        "DESCRIPTION": "Boilerplate for Django REST API",
        "VERSION": "1.0.0",
        "SERVE_INCLUDE_SCHEMA": False,
    }

    if not DEBUG:
        REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (
            "rest_framework.renderers.JSONRenderer",
        )

    TEMPLATES = [
        {
            "BACKEND": "django.template.backends.django.DjangoTemplates",
            "DIRS": [],
            "APP_DIRS": True,
            "OPTIONS": {
                "context_processors": [
                    "django.template.context_processors.debug",
                    "django.template.context_processors.request",
                    "django.contrib.auth.context_processors.auth",
                    "django.contrib.messages.context_processors.messages",
                ],
            },
        },
    ]

    AUTH_PASSWORD_VALIDATORS = [
        {
            "NAME": (
                "django.contrib.auth.password_validation."
                "UserAttributeSimilarityValidator"
            ),
        },
        {
            "NAME": (
                "django.contrib.auth.password_validation."
                "MinimumLengthValidator"
            ),
        },
        {
            "NAME": (
                "django.contrib.auth.password_validation."
                "CommonPasswordValidator"
            ),
        },
        {
            "NAME": (
                "django.contrib.auth.password_validation."
                "NumericPasswordValidator"
            ),
        },
    ]

    LANGUAGE_CODE = "en-us"
    TIME_ZONE = "UTC"
    USE_I18N = True
    USE_L10N = True
    USE_TZ = True

    # Database
    DATABASES = values.DatabaseURLValue(
        f"sqlite:///{BASE_DIR.parent / 'db.sqlite3'}"
    )
    CACHES = values.CacheURLValue("locmem://")
    SESSION_ENGINE = "django.contrib.sessions.backends.cache"
    SESSION_CACHE_ALIAS = "default"

    CHANNEL_LAYERS: dict[str, Any] = {
        "default": {"BACKEND": "channels.layers.InMemoryChannelLayer"}
    }

    CACHE_CONN_STRING = "redis://"


class Dev(Base):
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("RDS_DB_NAME", "postgres"),
            "USER": os.environ.get("RDS_USERNAME", "postgres"),
            "PASSWORD": os.environ.get("RDS_PASSWORD", "password"),
            "HOST": os.environ.get("RDS_HOSTNAME", "your-db-endpoint"),
            "PORT": os.environ.get("RDS_PORT", "5432"),
        }
    }

    CACHE_CONN_STRING = (
        f"redis://{os.environ.get('REDIS_USER', 'default')}"
        f":{os.environ.get('REDIS_PASSWORD', '')}"
        f"@{os.environ.get('REDIS_ENDPOINT', 'redis')}:6379/0"
    )
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": CACHE_CONN_STRING,
            "OPTIONS": {"CLIENT_CLASS": "django_redis.client.DefaultClient"},
        }
    }
    STORAGES = {
        "default": {
            "BACKEND": "django.core.files.storage.FileSystemStorage",
        },
        "staticfiles": {
            "BACKEND": (
                "whitenoise.storage.CompressedManifestStaticFilesStorage"
            ),
        },
    }


class Staging(Dev):
    SECRET_KEY = values.SecretValue()
    DEBUG = values.BooleanValue(False)
    SECURE_SSL_REDIRECT = values.BooleanValue(True)

    ALLOWED_HOSTS = ["api.some-stage-url.com"]
    CORS_ALLOWED_ORIGINS = [
        "https://dashboard.some-stage-url.com",
    ]
    CSRF_TRUSTED_ORIGINS = CORS_ALLOWED_ORIGINS
    SECURE_SSL_HOST = ALLOWED_HOSTS[0]
    MIDDLEWARE = Base.MIDDLEWARE[1:]
