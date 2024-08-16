from django.db import models
from solo.models import SingletonModel


class Contact(SingletonModel):
    address = models.CharField('Адрес храма', max_length=255)
    mobile_phone = models.CharField('Мобильный телефон', max_length=24)
    phone = models.CharField('Городской телефон', max_length=24, blank=True, null=True)
    email = models.EmailField('Электронная почта', blank=True, null=True)
    map = models.TextField(
        'Скрипт с картой',
        blank=True,
        null=True,
        help_text='Выбрать или скрипт или изображение! Вставить код карты яндекса, который начинается <script>...</script>. Создать такую можно тут https://yandex.ru/map-constructor',
    )
    image_map = models.ImageField(
        'Выбрать или скрипт или изображение! Изображение карты',
        upload_to='about/contacts/map',
        blank=True,
        null=True,
    )

    def __str__(self):
        return 'Контакты храма'

    class Meta:
        verbose_name = 'Контакты храма'


class Requisites(models.Model):
    """Банковские реквизиты"""

    inn = models.CharField('ИНН', max_length=50)
    checkpoint = models.CharField('КПП', max_length=50)
    ogrn = models.CharField('ОГРН', max_length=50)
    okpo = models.CharField('ОКПО', max_length=50)
    current_account = models.CharField('Расчетный счет', max_length=50)
    bank = models.CharField('Банк', max_length=255)
    bic = models.CharField('БИК', max_length=50)
    correspondent_account = models.CharField('Кор. счет', max_length=50)
    name_payee = models.CharField('Наименование получателя платежа', max_length=255)
    purpose_payment = models.CharField('Назначение платежа', max_length=255)
    qr_code = models.ImageField('QR код', upload_to='about/qr_codes', blank=True, null=True)

    def __str__(self):
        return f'{self.current_account}'

    class Meta:
        verbose_name = 'Банковские реквизиты'
        verbose_name_plural = 'Банковские реквизиты'
