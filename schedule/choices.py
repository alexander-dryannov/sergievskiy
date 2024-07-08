# TODO: Не нужно?
from django.db import models


class ServiceType(models.TextChoices):
    """Виды службы"""

    AKATHIST = 'Akathist', 'Акафист'
    ALL_NIGHT_VIGIL = 'All-night vigil', 'Всенощное бдение'
    DIVINE_LITURGY = 'Divine Liturgy', 'Божественная литургия'
    EARLY_DIVINE_LITURGY = 'Early Divine Liturgy', 'Ранняя Божественная литургия'
    LATE_DIVINE_LITURGY = 'Late Divine Liturgy', 'Поздняя Божественная литургия'
    Lithium = 'Lithium', 'Лития'
    MEMORIAL_SERVICE = 'Memorial service', 'Панихида'
    PRAYER_SERVICE = 'Prayer service', 'Молебен'
