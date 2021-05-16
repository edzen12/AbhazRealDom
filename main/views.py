from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import City, PostRentSale, ImageShots, Reviews



def index(request):

    filter_city = request.GET.get("city")
    # CHOICES
    filter_rent_sale = request.GET.get("rent_sale")
    filter_type_property = request.GET.get("type_property")

    filter_price_first = request.GET.get('first_price')
    filter_price_second = request.GET.get('second_price')
    filter_area_first = request.GET.get('area_first')
    filter_area_second = request.GET.get('area_second')

    print(filter_city)
    print(filter_rent_sale)
    print(filter_type_property)

    if 'search' in request.GET:
        if filter_city == 'Не выбрано':
            filter_city = False

        # CHOICES
        if filter_rent_sale == 'Не выбрано':
            filter_rent_sale = False
        
        if filter_type_property == 'Не выбрано':
            filter_type_property = False

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
        if filter_price_second:
            postrentsale = PostRentSale.objects.filter(
                Q(price__lte=int(filter_price_second)
                ))
        if filter_price_first:
            postrentsale = PostRentSale.objects.filter(
                Q( price__gte=int(filter_price_first)
                ))

        if filter_city:
            postrentsale = PostRentSale.objects.filter(
                Q(city=filter_city)
            )
        # CHOICES
        if filter_rent_sale:
            postrentsale = PostRentSale.objects.filter(
                Q(rent_sale=filter_rent_sale)
            )
        if filter_type_property:
            postrentsale = PostRentSale.objects.filter(
                Q(type_property=filter_type_property)
            )
    else:
        city = City.objects.all()
        postrentsale = PostRentSale.objects.all()
    
    return render(request, 'index.html', locals())


def reviews(request):
    reviews = Reviews.objects.all()
    context = {
        'reviews': reviews,
    }
    return render(request, 'pages/reviews.html', context)


def about(request):
    return render(request, 'pages/about.html')


def projects(request):
    return render(request, 'pages/projects.html')