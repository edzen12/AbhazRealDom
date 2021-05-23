from django.conf import settings
from django.core.mail import EmailMessage

from abhaz.celery import app



@app.task
def send_info(type_property, own, city, areas, floor, price, number):
    message = f"""
    Ваш объект: {type_property}
    Собственность\ Не оформлено: {own}
    Город \ район: {city}
    Площадь кв\м, сотки: {areas}
    Этаж \ этажность: {floor}
    Цена: {price}
    Номер телефона: {number}
    """
    email = EmailMessage(
        "ЮГ НЕДВИЖИМОСТЬ АБХАЗИЯ!",
        message, settings.EMAIL_HOST_USER,
        ['oichiev.edzen@gmail.com', 'yug_realty_abkhazia@mail.ru'],
    )
    email.send(fail_silently=False)

