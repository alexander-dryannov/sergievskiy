from django.db import models


class ServiceTypeEnum(models.TextChoices):
    PRAYER_SERVICE = 'Prayer service', 'Молебен'
    LITHIUM = 'Lithium', 'Лития'
    MEMORIAL_SERVICE = 'Memorial service', 'Панихида'
    AKATHIST = 'Akathist', 'Акафист'
    VESPERS = 'Vespers', 'Вечерня'
    MATINS = 'Matins', 'Утреня'
    ALL_NIGHT_VIGIL = 'All-night vigil', 'Всенощное бдение'
    WATCH = 'Watch', 'Часы'
    LITURGY = 'Liturgy', 'Божественная литургия'
    COMPLINE = 'Compline', 'Повечерие'
    MIDNIGHT = 'Midnight', 'Полунощница'
