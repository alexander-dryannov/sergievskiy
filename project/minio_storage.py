import os

from dotenv import load_dotenv
from minio import Minio


load_dotenv()

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
