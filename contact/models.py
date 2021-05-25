from django.db import models


# объект
TYPE_PROPERTY = (
    ('Квартира', 'Квартира'),
    ('Дом', 'Дом'),
    ('Участок', 'Участок'),
    ('Коммерческая недвижимость', 'Коммерческая недвижимость'),
)

# Собственность\ не оформлено
OWN = (
    ('Собственность', 'Собственность'),
    ('Не оформлено', 'Не оформлено'),
)

class Contact(models.Model):
    type_property = models.CharField(
        max_length=255, 
        verbose_name="Ваши Объекты", 
        choices=TYPE_PROPERTY, 
        blank=True, null=True
    )
    own = models.CharField(
        max_length=255, 
        verbose_name="Собственность\ не оформлено", 
        choices=OWN, 
        blank=True, null=True
    )
    city = models.CharField(
        max_length=255, 
        verbose_name="Город \ район",
    )
    areas = models.CharField(
        max_length=255, 
        verbose_name="Площадь кв\м, сотки", 
        blank=True, null=True
    )
    floor = models.CharField(
        max_length=255, 
        verbose_name="Этаж \ этажность",
        blank=True, null=True
    )
    price = models.DecimalField(
        verbose_name="Цена", 
        max_digits=10, decimal_places=2, 
        blank=True, null=True
    )
    number = models.CharField(
        max_length=255, 
        verbose_name="Номер телефона",
    )

    def __str__(self):
        return f"{self.type_property} --- {self.city} --- {self.number} --- {self.price}"
