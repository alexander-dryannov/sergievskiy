from django.db import models
from django.urls import reverse
from snippets.models import models as smodels


class MultiMedia(smodels.BasicModel):
    title = models.CharField('Название', max_length=255)
    url = models.URLField('Ссылка на видео')

    def get_absolute_url(self):
        return reverse(
            'mmedia:detail',
            args=[
                self.pk,
            ],
        )

    def get_update_url(self):
        return reverse(
            'mmedia:update',
            args=[
                self.pk,
            ],
        )

    def get_deletion_url(self):
        return reverse(
            'mmedia:delete',
            args=[
                self.pk,
            ],
        )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ссылка'
        verbose_name_plural = 'Ссылки'
