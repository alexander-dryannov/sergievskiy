import os
import uuid

from django.db import transaction

from . import choices, models


def create(files, album, is_deleted=False, is_visible=True):
    file_type = choices.FileType.IMAGE.value

    with transaction.atomic():
        for file in files:
            _, file_ext = os.path.splitext(file.name)
            file.name = f'{uuid.uuid4().hex}.{file_ext}'

            if file_ext in choices.VIDEO_EXTENSIONS:
                file_type = choices.FileType.VIDEO.value

            models.AlbumContent.objects.create(
                album=album,
                file=file,
                is_deleted=is_deleted,
                is_visible=is_visible,
                file_type=file_type,
            )
    return True
