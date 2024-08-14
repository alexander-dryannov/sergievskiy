# Generated by Django 5.1 on 2024-08-14 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='typy_post',
            new_name='type_post',
        ),
        migrations.AddField(
            model_name='post',
            name='is_fixed',
            field=models.BooleanField(default=False, verbose_name='Закрепленный пост'),
        ),
    ]
