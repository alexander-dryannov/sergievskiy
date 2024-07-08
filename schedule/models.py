from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from snippets.models.models import BasicModel


class Week(BasicModel):
    """Седмица (неделя)"""

    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Седмица'
        verbose_name_plural = 'Седмицы'


class ServiceType(BasicModel):
    """Тип службы"""

    name = models.CharField('Название службы', max_length=255, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип службы'
        verbose_name_plural = 'Тип служб'


class Schedule(BasicModel):
    """Расписание"""

    week = models.ForeignKey(
        Week, related_name='weeks', verbose_name='Седмица', on_delete=models.PROTECT
    )
    event = models.DateTimeField('Дата и время события')
    to_whom = models.TextField(
        'Кому служба',
    )
    type_service = models.ManyToManyField(
        ServiceType, related_name='services', verbose_name='Тип службы'
    )

    def __str__(self):
        return f'{self.event}'

    class Meta:
        verbose_name = 'Расписание богослужений'
        verbose_name_plural = 'Расписание богослужений'
