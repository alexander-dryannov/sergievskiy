from django.db import models
from django.urls import reverse

from snippets.models import models as smodels

from . import choices


class Album(smodels.FileModel):
    title = models.CharField('Название альбома', max_length=255)
    cover = models.ImageField('Обложка', upload_to='covers/%Y/%m/%d')

    def get_absolute_url(self):
        return reverse(
            'gallery:album_detail',
            args=[
                self.pk,
            ],
        )

    def get_update_url(self):
        return reverse(
            'gallery:album_update',
            args=[
                self.pk,
            ],
        )

    def get_deletion_url(self):
        return reverse(
            'gallery:album_delete',
            args=[
                self.pk,
            ],
        )

    def get_deletion_to_cart_url(self):
        return reverse(
            'gallery:album_delete_to_cart',
            args=[
                self.pk,
            ],
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Альбом'
        verbose_name_plural = 'Альбомы'


class AlbumContent(smodels.FileModel):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file = models.ImageField('Изображение', upload_to='images/%Y/%m/%d')
    file_type = models.CharField(
        'Тип контента',
        default=choices.FileType.IMAGE.value,
        choices=choices.FileType.choices,
        max_length=20,
    )

    def get_absolute_url(self):
        return reverse(
            'gallery:content_detail',
            args=[
                self.album_id,
                self.slug,
            ],
        )

    def get_update_url(self):
        return reverse(
            'gallery:content_update',
            args=[
                self.album_id,
                self.slug,
            ],
        )

    def get_deletion_url(self):
        return reverse(
            'gallery:content_delete',
            args=[
                self.album_id,
                self.slug,
            ],
        )

    def get_deletion_to_cart_url(self):
        return reverse(
            'gallery:content_delete_to_cart',
            args=[
                self.album_id,
                self.slug,
            ],
        )

    def __str__(self):
        return f'# {self.pk}'

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'
