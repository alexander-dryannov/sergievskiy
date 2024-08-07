from django.conf import settings


client = settings.MINIO_CLIENT


def delete_object(obj: str | list, bucket: str = settings.MINIO_STORAGE_MEDIA_BUCKET_NAME) -> None:
    if isinstance(obj, str):
        if obj:
            client.remove_object(bucket, obj)

    if isinstance(obj, list | set):
        for item in obj:
            client.remove_object(bucket, item)
