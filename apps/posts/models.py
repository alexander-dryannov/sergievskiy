from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from snippets.models.models import BasicModel

USER = get_user_model()


class TypePostEnum(models.TextChoices):
    EVENT = (
        'event',
        'Событие',
    )
    HELP = (
        'help',
        'Помощь',
    )
    NEWS = (
        'news',
        'Новость',
    )
    ADVERTISEMENT = (
        'advertisement',
        'Объявление',
    )
    FREE = (
        'free',
        'Без темы',
    )


class Post(BasicModel):
    author = models.ForeignKey(
        USER, verbose_name='Автор', related_name='+', on_delete=models.PROTECT
    )
    title = models.CharField('Название', max_length=100)
    text = models.TextField('Текст')
    type_post = models.CharField(
        'Тип поста', choices=TypePostEnum.choices, default=TypePostEnum.NEWS, max_length=100
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Публикация'
        verbose_name_plural = 'Публикации'


class FixedPost(models.Model):
    target = models.ForeignKey(Post, verbose_name='Новость', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Закрепленная новость'
        verbose_name_plural = 'Закрепленные новости'
