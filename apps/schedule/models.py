from django.db import models

from snippets.models.models import BasicModel


class ServiceType(BasicModel):
    """Тип службы"""

    name = models.CharField('Тип службы')
    ordering = models.PositiveSmallIntegerField('Сортировка', default=0)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['ordering']
        verbose_name = 'Тип службы'
        verbose_name_plural = 'Типы служб'


class Week(BasicModel):
    """Неделя (седмица)"""

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
    """День"""

    week = models.ForeignKey(Week, verbose_name='Седмица', related_name='days', on_delete=models.PROTECT)
    date = models.DateField('Дата')
    to_whom = models.TextField('Кому служба', blank=True, null=True)
    is_holiday = models.BooleanField(
        'Праздник', default=False, help_text='Для окраски дня службы в красный'
    )

    def __str__(self):
        return f'{self.date.strftime('%d.%m.%Y')}'

    class Meta:
        verbose_name = 'Богослужебный день'
        verbose_name_plural = 'Богослужебные дни'


class Event(BasicModel):
    """Событие"""
    
    day = models.ForeignKey(Day, verbose_name='День', related_name='events', on_delete=models.PROTECT)
    type_service = models.ManyToManyField(ServiceType, verbose_name='Тип службы', blank=True)
    time = models.TimeField('Время')
    is_holiday = models.BooleanField(
        'Праздник', default=False, help_text='Для окраски дня службы в красный'
    )

    def __str__(self):
        return f'{self.day.date} | {self.time}'

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
