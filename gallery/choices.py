from django.db import models


class FileType(models.TextChoices):
    IMAGE = 'image', 'Изображение'
    VIDEO = 'video', 'Видео'


IMAGE_EXTENSIONS = ['.jpeg', '.jpg', '.png', '.webp', '.gif']

VIDEO_EXTENSIONS = ['.avi', '.mp4', '.mov', '.flv', '.mkv', '.webm']
