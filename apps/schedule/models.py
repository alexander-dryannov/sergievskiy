from django.db import models

from snippets.models.models import BasicModel


class ServiceType(BasicModel):
    name = models.CharField('Тип службы')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип службы'
        verbose_name_plural = 'Типы служб'


class Week(BasicModel):
    name = models.CharField('Название седмицы', max_length=100)
    short_name = models.CharField(
        'Короткое название седмицы', max_length=100, null=True, blank=True
    )

    def __str__(self):
        if self.short_name:
            return self.short_name
        return self.name

    class Meta:
        verbose_name = 'Седмица'
        verbose_name_plural = 'Седмицы'


class Day(BasicModel):
    week = models.ForeignKey(Week, verbose_name='Седмица', on_delete=models.PROTECT)
    date = models.DateField('Дата')

    def __str__(self):
        if self.week.short_name:
            return f'{self.week.short_name} | { self.date}'
        return f'{self.date}'

    class Meta:
        verbose_name = 'Богослужебный день'
        verbose_name_plural = 'Богослужебные дни'


class Event(BasicModel):
    day = models.ForeignKey(Day, verbose_name='День', on_delete=models.PROTECT)
    type_service = models.ManyToManyField(ServiceType, blank=True)
    time = models.TimeField('Время')
    to_whom = models.TextField('Кому служба', blank=True, null=True)

    def __str__(self):
        return f'{self.day.date} | {self.time}'

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
