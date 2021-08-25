from django.shortcuts import render 
from django.db.models import Q 
from .models import (City, PostRentSale, TypeProperty, RentSale)

# Фильтр и Главная страница
def index(request):

    filter_city = request.GET.get("city")
    filter_rent_sale = request.GET.get("rent_sale")
    filter_type_property = request.GET.get("type_property")
    # Цена и Аренда/Продажа
    filter_price_first = request.GET.get('first_price')
    filter_price_second = request.GET.get('second_price')
    filter_area_first = request.GET.get('area_first')
    filter_area_second = request.GET.get('area_second')

    if 'search' in request.GET:
        city = City.objects.all()
        rent_sale = RentSale.objects.all()
        postrentsale = PostRentSale.objects.all()
        type_property = TypeProperty.objects.all()

        if filter_city == 'Не выбрано':
            filter_city = False

        if filter_rent_sale == 'Не выбрано':
            filter_rent_sale = False

        if filter_type_property == 'Не выбрано':
            filter_type_property = False


        ### Фильтр Площади ###

        # первая площадь
        if filter_area_first:
            postrentsale = PostRentSale.objects.filter(
                Q(areas__gte=int(filter_area_first))
            )
        # вторая площадь
        if filter_area_second:
            postrentsale = PostRentSale.objects.filter(
                Q(areas__lte=int(filter_area_second))
            )
        # первая площадь и вторая площадь
        if filter_area_first and filter_area_second:
            postrentsale = PostRentSale.objects.filter(
                Q(areas__gte=int(filter_area_first), price__lte=int(filter_area_second))
            )
        # первая площадь и первая цена
        if filter_area_first and filter_price_first:
            postrentsale = PostRentSale.objects.filter(
                Q(areas__gte=int(filter_area_first), price__lte=int(filter_price_first))
            )
        # первая площадь и вторая цена
        if filter_area_first and filter_price_second:
            postrentsale = PostRentSale.objects.filter(
                Q(areas__gte=int(filter_area_first), price__lte=int(filter_price_second))
            )
        # вторая площадь и первая цена
        if filter_area_second and filter_price_first:
            postrentsale = PostRentSale.objects.filter(
                Q(areas__lte=int(filter_area_second), price__gte=int(filter_price_first))
            )
        # вторая площадь и вторая цена
        if filter_area_second and filter_price_second:
            postrentsale = PostRentSale.objects.filter(
                Q(areas__lte=int(filter_area_second), price__lte=int(filter_price_second))
            )
        # первая площадь и вторая площадь и первая цена
        if filter_area_first and filter_area_second and filter_price_first:
            postrentsale = PostRentSale.objects.filter(
                Q(areas__gte=int(filter_area_first), areas__lte=int(filter_area_second), price__gte=int(filter_price_first))
            )
        # первая площадь и вторая площадь и вторая цена
        if filter_area_first and filter_area_second and filter_price_second:
            postrentsale = PostRentSale.objects.filter(
                Q(areas__gte=int(filter_area_first), areas__lte=int(filter_area_second), price__lte=int(filter_price_second))
            )
        # Фильтр Аренда/Продажа и вторая площадь
        if filter_rent_sale and filter_area_second:
            postrentsale = PostRentSale.objects.filter(
                Q(rent_sale=filter_rent_sale, areas__lte=int(filter_area_second))
            )
        # Фильтр Аренда/Продажа и вторая цена
        if filter_rent_sale and filter_price_second:
            postrentsale = PostRentSale.objects.filter(
                Q(rent_sale=filter_rent_sale, price__lte=int(filter_price_second))
            )
        # Фильтр Аренда/Продажа и первая цена
        if filter_rent_sale and filter_price_first:
            postrentsale = PostRentSale.objects.filter(
                Q(rent_sale=filter_rent_sale, price__gte=int(filter_price_first))
            )
        # Фильтр Аренда/Продажа и первая цена
        if filter_price_first and filter_rent_sale:
            postrentsale = PostRentSale.objects.filter(
                Q(price__gte=int(filter_price_first)), Q(rent_sale=filter_rent_sale)
            )


        ### Фильтр Цены ###

        # вторая цена
        if filter_price_second:
            postrentsale = PostRentSale.objects.filter(
                Q(price__lte=int(filter_price_second))
            )
        # первая цена
        if filter_price_first:
            postrentsale = PostRentSale.objects.filter(
                Q( price__gte=int(filter_price_first))
            )
        # первая цена and вторая цена
        if filter_price_first and filter_price_second:
            postrentsale = PostRentSale.objects.filter(
                Q(price__gte=int(filter_price_first), price__lte=int(filter_price_second))
            )

        ### Фильтр Города ###

        # фильтр города
        if filter_city:
            postrentsale = PostRentSale.objects.filter(
                Q(city=filter_city)
            )
        # Фильтр Города и Аренда/Продажа
        if filter_city and filter_rent_sale:
            postrentsale = PostRentSale.objects.filter(
                Q(city=filter_city), Q(rent_sale=filter_rent_sale)
            )
        # Фильтр цена вторая и Аренда/Продажа
        if filter_price_second and filter_rent_sale:
            postrentsale = PostRentSale.objects.filter(
                Q(price__gte=filter_price_second), Q(rent_sale=filter_rent_sale)
            )
        # Фильтр цена first и Аренда/Продажа
        if filter_price_first and filter_rent_sale:
            postrentsale = PostRentSale.objects.filter(
                Q(price__lte=filter_price_first), Q(rent_sale=filter_rent_sale)
            )
        # Фильтр Города и Тип Недвижимости
        if filter_city and filter_type_property:
            postrentsale = PostRentSale.objects.filter(
                Q(city=filter_city), Q(type_property=filter_type_property)
            )
        # Фильтр Аренда/Продажа и Тип Недвижимости
        if filter_rent_sale and filter_type_property:
            postrentsale = PostRentSale.objects.filter(
                Q(rent_sale=filter_rent_sale), Q(type_property=filter_type_property)
            )
        # Фильтр Города и Аренда/Продажа и Тип Недвижимости
        if filter_city and filter_rent_sale and filter_type_property:
            postrentsale = PostRentSale.objects.filter(
                Q(city=filter_city), Q(rent_sale=filter_rent_sale), Q(type_property=filter_type_property)
            )

        ### Фильтр Аренда/Продажа  ###

        # Фильтр Аренда/Продажа
        if filter_rent_sale:
            postrentsale = PostRentSale.objects.filter(
                Q(rent_sale=filter_rent_sale)
            )
        # Фильтр Аренда/Продажа и Города
        if filter_rent_sale and filter_city:
            postrentsale = PostRentSale.objects.filter(
                Q(rent_sale=filter_rent_sale), Q(city=filter_city)
            )
        # Фильтр Аренда/Продажа и Города и Тип Недвижимости
        if filter_rent_sale and filter_city and filter_type_property:
            postrentsale = PostRentSale.objects.filter(
                Q(rent_sale=filter_rent_sale), Q(city=filter_city), Q(type_property=filter_type_property)
            )
        # Фильтр Тип Недвижимости
        if filter_type_property:
            postrentsale = PostRentSale.objects.filter(
                Q(type_property=filter_type_property)
            )
        # Фильтр Тип Недвижимости \\ Города
        if filter_type_property and filter_city:
            postrentsale = PostRentSale.objects.filter(
                Q(type_property=filter_type_property), Q(city=filter_city)
            )
        # Фильтр Тип Недвижимости \\ Города \\ Аренда/Продажа
        if filter_type_property and filter_city and filter_rent_sale:
            postrentsale = PostRentSale.objects.filter(
                Q(type_property=filter_type_property), Q(city=filter_city), Q(rent_sale=filter_rent_sale)
            )
        # Фильтр по 7 START
        if filter_price_first and filter_price_second and filter_area_first and filter_area_second and filter_city and filter_rent_sale and filter_type_property:
            postrentsale = PostRentSale.objects.filter(
                Q(price__gte=int(filter_price_first), price__lte=int(filter_price_second)), 
                Q(areas__lte=int(filter_area_second), areas__gte=int(filter_area_first)),
                Q(city=filter_city), 
                Q(rent_sale=filter_rent_sale),
                Q(type_property=filter_type_property),
            )
        # Фильтр по 7 END
        # Фильтр по 6 START
        if filter_price_first and filter_price_second and filter_area_first and filter_area_second and filter_rent_sale and filter_type_property:
            postrentsale = PostRentSale.objects.filter(
                Q(price__gte=int(filter_price_first), price__lte=int(filter_price_second)), 
                Q(areas__lte=int(filter_area_second), areas__gte=int(filter_area_first)), 
                Q(rent_sale=filter_rent_sale),
                Q(type_property=filter_type_property)
            )
        # Фильтр по 6 END
        # Фильтр по 6 START
        if filter_price_first and filter_price_second and filter_area_first and filter_area_second and filter_city and filter_type_property:
            postrentsale = PostRentSale.objects.filter(
                Q(price__gte=int(filter_price_first), price__lte=int(filter_price_second)), 
                Q(areas__lte=int(filter_area_second), areas__gte=int(filter_area_first)), 
                Q(city=filter_city),
                Q(type_property=filter_type_property)
            )
        # Фильтр по 6 END
        # Фильтр по 5 START
        if filter_price_first and filter_price_second and filter_area_first and filter_area_second and filter_rent_sale:
            postrentsale = PostRentSale.objects.filter(
                Q(price__gte=int(filter_price_first), price__lte=int(filter_price_second)), 
                Q(areas__gte=int(filter_area_first), areas__lte=int(filter_area_second)),
                Q(rent_sale=filter_rent_sale)
            )
        # Фильтр по 5 END
        # Фильтр по 5 START
        if filter_price_first and filter_price_second and filter_area_first and filter_area_second and filter_type_property:
            postrentsale = PostRentSale.objects.filter(
                Q(price__gte=int(filter_price_first), price__lte=int(filter_price_second)), 
                Q(areas__gte=int(filter_area_first), areas__lte=int(filter_area_second)),
                Q(type_property=filter_type_property)
            )
        # Фильтр по 5 END
        # Фильтр по 5 START
        if filter_price_first and filter_price_second and filter_area_first and filter_area_second and filter_city:
            postrentsale = PostRentSale.objects.filter(
                Q(price__gte=int(filter_price_first), price__lte=int(filter_price_second)), 
                Q(areas__gte=int(filter_area_first), areas__lte=int(filter_area_second)),
                Q(city=filter_city)
            )
        # Фильтр по 5 END
    else:
        city = City.objects.all()
        rent_sale = RentSale.objects.all()
        postrentsale = PostRentSale.objects.all().order_by('-id')[:4]
        postrentsale_vip = PostRentSale.objects.filter(vip='Да').order_by('-id')[:8]
        type_property = TypeProperty.objects.all()

    page="home"
    return render(request, 'index.html', locals())

