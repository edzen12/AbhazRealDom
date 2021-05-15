from django.db import models
from .choice import *


# Город
class City(models.Model):
    title = models.CharField(
        max_length=255, verbose_name="Город", 
        blank=True, null=True
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = "город"
        verbose_name_plural = "Города"


# Все Объекты
class RSObjects(models.Model):

    title = models.CharField(
        max_length=255, verbose_name="Название", blank=True, null=True,
    )
    image = models.ImageField(
        verbose_name="Фото", blank=True, null=True, upload_to="dom/"
    )
    city = models.ForeignKey(
        City, on_delete=models.CASCADE,  verbose_name="Город",
        null=True, blank=True
    )
    rent_sale = models.CharField(
        max_length=255, choices=RENT_SALE, 
        verbose_name="Аренда/Продажа", blank=True, null=True,
    )
    rs_objects = models.CharField(
        max_length=255, choices=OBJECTS_CHOICES,
        verbose_name="Объекты", blank=True, null=True,
        help_text="Например: Дома; Квартиры; Участки; Коммерческая недвижимость"
    )
    status = models.CharField(
        max_length=255, choices=STATUS, 
        verbose_name="Состояние", blank=True, null=True,
    )
    dom_type = models.CharField(
        max_length=255, choices=DOM_TYPE, 
        verbose_name="Тип дома", blank=True, null=True,
    )
    material_type = models.CharField(
        max_length=255, choices=MATERIAL_TYPE,
        verbose_name="Тип материала", blank=True, null=True,
    )
    floors = models.CharField(
        max_length=255, verbose_name="Этаж / этажность", 
        blank=True, null=True, help_text="пример: 3 / 5"
    )
    rooms = models.IntegerField(
        verbose_name="Кол-во комнат", blank=True, null=True,
    )
    areas = models.IntegerField(
        verbose_name="Площадь м²", blank=True, null=True,
    )
    height_ceiling = models.IntegerField(
        verbose_name="Высота потолков м²", blank=True, null=True,
    )
    price = models.DecimalField(
        verbose_name="Цена в рублях", max_digits=10, decimal_places=2, 
        blank=True, null=True
    )
    region = models.CharField(
        max_length=255, verbose_name="Район", blank=True, null=True,
    )
    year_built = models.DateField(
        verbose_name="Год постройки", blank=True, null=True,
    )
    distance_sea = models.CharField(
        verbose_name='Расстояние до море', max_length=255,
        blank=True, null=True
    )
    distance_track = models.CharField(
        verbose_name='Расстояние до трассы', max_length=255, 
        blank=True, null=True
    )
    ownership = models.CharField(
        verbose_name='Право собственности', max_length=50, 
        blank=True, null=True
    )
    description = models.TextField(
        verbose_name='Описание', blank=True, null=True
    )
    vip = models.CharField(
        verbose_name="VIP", choices=VIP, max_length=255, 
        blank=True, null=True, default=2
    )
    slug = models.SlugField(max_length=255, unique=True, blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "объект"
        verbose_name_plural = "Объекты"


class ImageShots(models.Model):
    image = models.ImageField("Изображение", upload_to="image_shots/")
    rs_objects = models.ForeignKey(RSObjects, verbose_name="Объекты", on_delete=models.CASCADE)

    class Meta:
        verbose_name = "фотка"
        verbose_name_plural = "Фотки"


class Reviews(models.Model):
    nikname = models.CharField(verbose_name='Никнейм', max_length=255)
    desc = models.TextField(
        verbose_name='Описание', blank=True, null=True
    )
    image = models.ImageField(
        verbose_name='Фото', upload_to="reviews/", blank=True, null=True
    )
    video = models.FileField(
        verbose_name='Видео', blank=True, null=True, upload_to='video/'
    )
    date = models.DateField(verbose_name='Дата')

    def __str__(self):
        return self.nikname

    class Meta:
        verbose_name = 'отзыв'
        verbose_name_plural = 'Отзывы'


