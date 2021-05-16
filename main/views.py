from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View
from django.db.models import Q
from .models import (
    City, PostRentSale, Reviews, 
    ImageShots, TypeProperty, RentSale
)



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
        if filter_city == 'Не выбрано':
            filter_city = False

        if filter_rent_sale == 'Не выбрано':
            filter_rent_sale = False
        
        if filter_type_property == 'Не выбрано':
            filter_type_property = False

        # Фильтр Площади
        if filter_price_first and filter_price_second:
            postrentsale = PostRentSale.objects.filter(
                Q(price__gte=int(filter_price_first), price__lte=int(filter_price_second)
                ))
        if filter_area_first and filter_area_second:
            postrentsale = PostRentSale.objects.filter(
                Q(areas__gte=int(filter_area_first), areas__lte=int(filter_area_second)
                ))
        if filter_area_first:
            postrentsale = PostRentSale.objects.filter(
                Q(areas__gte=int(filter_area_first)
                ))
        if filter_area_second:
            postrentsale = PostRentSale.objects.filter(
                Q(areas__lte=int(filter_area_second)
                ))

        # Фильтр Цены
        if filter_price_second:
            postrentsale = PostRentSale.objects.filter(
                Q(price__lte=int(filter_price_second)
                ))
        if filter_price_first:
            postrentsale = PostRentSale.objects.filter(
                Q( price__gte=int(filter_price_first)
                ))

        # Фильтр Города
        if filter_city:
            postrentsale = PostRentSale.objects.filter(
                Q(city=filter_city)
            )
        # Фильтр Аренда/Продажа
        if filter_rent_sale:
            postrentsale = PostRentSale.objects.filter(
                Q(rent_sale=filter_rent_sale)
            )
        # Фильтр Тип Недвижимости
        if filter_type_property:
            postrentsale = PostRentSale.objects.filter(
                Q(type_property=filter_type_property)
            )
    else:
        city = City.objects.all()
        rent_sale = RentSale.objects.all()
        postrentsale = PostRentSale.objects.all()
        type_property = TypeProperty.objects.all()
    
    page="home"
    return render(request, 'index.html', locals())


class PostRentSaleDetailView(View):
    def get(self, request, slug):
        postrentsale = PostRentSale.objects.get(slug=slug)
        rentsale = PostRentSale.objects.all().order_by('?')[:4]
        context = {
            'postrentsale': postrentsale,
            'rentsale': rentsale
        }
        return render(request, "pages/postrentsale_detail.html", context)


def reviews(request):
    reviews = Reviews.objects.all()
    context = {
        'reviews': reviews,
    }
    page="reviews"
    return render(request, 'pages/reviews.html', context)


class ReviewsDetailView(View):
    def get(self, request, slug):
        reviews = Reviews.objects.get(slug=slug)
        context = {
            'reviews': reviews,
        }
        page="reviews"
        return render(request, "pages/reviews_detail.html", context)


def about(request):
    page="about"
    return render(request, 'pages/about.html')


def projects(request):
    page="projects"
    return render(request, 'pages/projects.html')