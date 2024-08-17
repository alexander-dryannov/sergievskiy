# Generated by Django 5.1 on 2024-08-16 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_remove_contact_maps_contact_image_map_contact_map_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Requisites',
            fields=[
                (
                    'id',
                    models.BigAutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name='ID'
                    ),
                ),
                ('inn', models.BigIntegerField(verbose_name='ИНН')),
                ('checkpoint', models.BigIntegerField(verbose_name='КПП')),
                ('ogrn', models.BigIntegerField(verbose_name='ОГРН')),
                ('okpo', models.BigIntegerField(verbose_name='ОКПО')),
                ('current_account', models.BigIntegerField(verbose_name='Расчетный счет')),
                ('bank', models.CharField(max_length=255, verbose_name='Банк')),
                ('bic', models.BigIntegerField(verbose_name='БИК')),
                ('correspondent_account', models.BigIntegerField(verbose_name='Кор. счет')),
                (
                    'name_payee',
                    models.CharField(
                        max_length=255, verbose_name='Наименование получателя платежа'
                    ),
                ),
                (
                    'purpose_payment',
                    models.CharField(max_length=255, verbose_name='Назначение платежа'),
                ),
            ],
            options={
                'verbose_name': 'Банковские реквизиты',
                'verbose_name_plural': 'Банковские реквизиты',
            },
        ),
    ]