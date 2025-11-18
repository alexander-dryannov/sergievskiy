import os
from pathlib import Path

from dotenv import load_dotenv
from minio import Minio


load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv('SECRET_KEY')

SITE_NAME = os.getenv('SITE_NAME', 'sergievskiy.backend')

SITE_IP = os.getenv('SITE_IP', '127.0.0.1')

DEBUG = os.environ.get('DEBUG', False) == 'True'

ALLOWED_HOSTS = [f'http://{SITE_NAME}', f'https://{SITE_NAME}', SITE_IP]

CSRF_TRUSTED_ORIGINS = []

if DEBUG:
    ALLOWED_HOSTS.append('*')
    CORS_ALLOW_ALL_ORIGINS = bool(DEBUG)
else:
    CSRF_TRUSTED_ORIGINS += [f'http://{SITE_NAME}', f'https://{SITE_NAME}']

ALLOWED_HOSTS = list(set(ALLOWED_HOSTS))

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'minio_storage',
    'solo',
    'crispy_forms',
    'crispy_bootstrap5',
    # 'apps.gallery',
    # 'apps.multimedia',
    'apps.schedule',
    'apps.posts',
    'apps.about',
    'debug_toolbar',
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

INTERNAL_IPS = [
    'localhost',
    '127.0.0.1',
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'template',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'

if os.getenv('ENGINE'):
    DATABASES = {
        'default': {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": os.environ.get("DB_NAME"),
            "USER": os.environ.get("DB_USER"),
            "PASSWORD": os.environ.get("DB_PASSWORD"),
            "HOST": os.environ.get("DB_HOST", "127.0.0.1"),
            "PORT": os.environ.get("DB_PORT", 5432),
        }
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'Europe/Moscow'

USE_I18N = True

USE_TZ = False

MINIO_STATIC = os.environ.get('MINIO_STATIC', False) == 'True'

MINIO_MEDIA = os.environ.get('MINIO_MEDIA', False) == 'True'

MINIO = os.environ.get('MINIO', False) == 'True'

STATIC_URL = 'static/'

STATIC_ROOT = 'staticfiles'

STATICFILES_DIRS = ['static']

if not MINIO_MEDIA:
    MEDIA_URL = 'media/'
    # MEDIA_ROOT = 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Количество постов на странице
POSTS_PAGE_SIZE = os.environ.get('POSTS_PAGE_SIZE', 5)

CRISPY_ALLOWED_TEMPLATE_PACKS = 'bootstrap5'

CRISPY_TEMPLATE_PACK = 'bootstrap5'

MINIO_CLIENT = False

if MINIO:
    DEFAULT_FILE_STORAGE = 'minio_storage.storage.MinioMediaStorage'

    MINIO_STATIC = os.environ.get('MINIO_STATIC', False) == 'True'

    MINIO_MEDIA = os.environ.get('MINIO_MEDIA', False) == 'True'

    if MINIO_STATIC:
        STATICFILES_STORAGE = 'minio_storage.storage.MinioStaticStorage'
        MINIO_STORAGE_STATIC_BUCKET_NAME = os.getenv(
            'MINIO_STORAGE_STATIC_BUCKET_NAME', 'dev-sergievskiy-static'
        )
        MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = (
                os.environ.get('MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET', False) == 'True'
        )

    if MINIO_MEDIA:
        MINIO_STORAGE_MEDIA_BUCKET_NAME = os.getenv(
            'MINIO_STORAGE_MEDIA_BUCKET_NAME', 'dev-sergievskiy-media'
        )
        MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = (
                os.environ.get('MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET', False) == 'True'
        )

    MINIO_STORAGE_ACCESS_KEY = os.getenv('MINIO_STORAGE_ACCESS_KEY')
    MINIO_STORAGE_SECRET_KEY = os.getenv('MINIO_STORAGE_SECRET_KEY')
    MINIO_STORAGE_USE_HTTPS = os.environ.get('MINIO_STORAGE_USE_HTTPS', False) == 'True'
    MINIO_STORAGE_ENDPOINT = os.getenv('MINIO_STORAGE_ENDPOINT')

    MINIO_CLIENT = Minio(
        MINIO_STORAGE_ENDPOINT,
        MINIO_STORAGE_ACCESS_KEY,
        MINIO_STORAGE_SECRET_KEY,
        secure=True if MINIO_STORAGE_USE_HTTPS else False,
    )

REDIS_HOST = os.getenv('REDIS_HOST', 'localhost')
REDIS_PORT = int(os.getenv('REDIS_PORT', '6379'))
REDIS_USERNAME = os.getenv('REDIS_USERNAME')
REDIS_PASSWORD = os.getenv('REDIS_PASSWORD', None) or None
REDIS_DB_CACHE = os.getenv('REDIS_DB_CACHE', 0)
REDIS_CACHE_TIMEOUT = int(os.getenv('REDIS_CACHE_TIMEOUT', 10)) * 60

CACHES = {
    "default": {
        "BACKEND": 'django.core.cache.backends.redis.RedisCache',
        "LOCATION": f'redis://{REDIS_HOST}:{REDIS_PORT}',
        "OPTIONS": {
            "db": REDIS_DB_CACHE
        },
    }
}