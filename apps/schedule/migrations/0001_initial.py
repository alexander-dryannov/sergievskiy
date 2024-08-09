# Generated by Django 5.0.6 on 2024-07-08 14:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name='ServiceType',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Видимый')),
                (
                    'name',
                    models.CharField(max_length=255, unique=True, verbose_name='Название службы'),
                ),
            ],
            options={
                'verbose_name': 'Тип службы',
                'verbose_name_plural': 'Тип служб',
            },
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Видимый')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Седмица',
                'verbose_name_plural': 'Седмицы',
            },
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создано')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Обновлено')),
                ('is_visible', models.BooleanField(default=True, verbose_name='Видимый')),
                ('event', models.DateTimeField(verbose_name='Дата и время события')),
                ('to_whom', models.TextField(verbose_name='Кому служба')),
                (
                    'type_service',
                    models.ManyToManyField(
                        related_name='services',
                        to='schedule.servicetype',
                        verbose_name='Тип службы',
                    ),
                ),
                (
                    'week',
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name='weeks',
                        to='schedule.week',
                        verbose_name='Седмица',
                    ),
                ),
            ],
            options={
                'verbose_name': 'Расписание богослужений',
                'verbose_name_plural': 'Расписание богослужений',
            },
        ),
    ]