from django.db import models
from solo.models import SingletonModel

from snippets.models.models import BasicModel


class Contact(SingletonModel):
    """Контакты"""

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


class DignityEnum(models.TextChoices):
    """Саны православной церкви"""

    ARCHDEACON = 'Archdeacon', 'Архидьякон'
    ARCHBISHOP = 'Archbishop', 'Архиепископ'
    ARCHIMANDRITE = 'Archimandrite', 'Архимандрит'
    DEACON = 'Deacon', 'Дьякон'
    BISHOP = 'Bishop', 'Епископ'
    ABBOT = 'Abbot', 'Игумен'
    PRIEST = 'Priest', 'Иерей'
    HIERODEACON = 'Hierodeacon', 'Иеродиакон'
    HIEROMONK = 'Hieromonk', 'Иеромонах'
    METROPOLITAN = 'Metropolitan', 'Митрополит'
    PATRIARCH = 'Patriarch', 'Патриарх'
    PROTODEACON = 'Protodeacon', 'Протодьякон'
    ARCHPRIEST = 'Archpriest', 'Протоиерей'
    PROTOPRESBYTER = 'Protopresbyter', 'Протопресвитер'


class Clergy(BasicModel):
    """Духовенство"""

    last_name = models.CharField('Фамилия', max_length=50)
    first_name = models.CharField('Имя', max_length=50)
    middle_name = models.CharField('Отчество', max_length=50)
    birthday = models.DateField('День рождения')
    photo = models.ImageField('Фотография', upload_to='about/clergy', blank=True, null=True)
    rector_temple = models.BooleanField('Настоятель храма', default=False)
    dignity = models.CharField(
        'Сан', choices=DignityEnum.choices, default=DignityEnum.PRIEST, max_length=50
    )
    secular_education = models.CharField(
        'Светское образование', max_length=100, blank=True, null=True
    )
    spiritual_education = models.CharField(
        'Духовное образование', max_length=100, blank=True, null=True
    )
    consecrated = models.CharField('Хиротонисан', max_length=20, blank=True, null=True)
    namesake_day = models.CharField('День тезоименитства', max_length=20, blank=True, null=True)

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    class Meta:
        verbose_name = 'Духовенство'
        verbose_name_plural = 'Духовенство'
