from django.shortcuts import render
from django.views.generic.base import View
from django.core.paginator import Paginator
from django.db.models import Q
from contact.forms import ContactForm
from .models import (
    City, PostRentSale, Reviews,
    ImageShots, TypeProperty, RentSale
)


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
                Q( price__gte=int(filter_price_first))
            )
        if filter_price_first and filter_price_second:
            postrentsale = PostRentSale.objects.filter(
                Q(price__gte=int(filter_price_first), price__lte=int(filter_price_second)
                ))

        # Фильтр Города
        if filter_city:
            postrentsale = PostRentSale.objects.filter(
                Q(city=filter_city)
            )
        # Фильтр Города \\ Аренда/Продажа
        if filter_city and filter_rent_sale:
            postrentsale = PostRentSale.objects.filter(
                Q(city=filter_city), Q(rent_sale=filter_rent_sale)
            )
        # Фильтр Города \\ Аренда/Продажа \\ Тип Недвижимости
        if filter_city and filter_rent_sale and filter_type_property:
            postrentsale = PostRentSale.objects.filter(
                Q(city=filter_city), Q(rent_sale=filter_rent_sale), Q(type_property=filter_type_property)
            )
        # Фильтр Аренда/Продажа
        if filter_rent_sale:
            postrentsale = PostRentSale.objects.filter(
                Q(rent_sale=filter_rent_sale)
            )
        # Фильтр Аренда/Продажа \\ Города
        if filter_rent_sale and filter_city:
            postrentsale = PostRentSale.objects.filter(
                Q(rent_sale=filter_rent_sale), Q(city=filter_city)
            )
        # Фильтр Аренда/Продажа \\ Города \\ Тип Недвижимости
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
    else:
        city = City.objects.all()
        rent_sale = RentSale.objects.all()
        postrentsale = PostRentSale.objects.all().order_by('-id')[:4]
        postrentsale_vip = PostRentSale.objects.filter(vip='Да').order_by('-id')[:8]
        type_property = TypeProperty.objects.all()

    page="home"
    return render(request, 'index.html', locals())


# Отдельная страница Поста
class PostRentSaleDetailView(View):
    def get(self, request, slug):
        postrentsale = PostRentSale.objects.get(slug=slug)
        imageshots = ImageShots.objects.all()
        rentsale = PostRentSale.objects.all().order_by('price')[:4]
        context = {
            'postrentsale': postrentsale,
            'rentsale': rentsale,
            'imageshots': imageshots
        }
        return render(request, "pages/postrentsale_detail.html", context)


# Аренда - Дома
def arenda_dom_page(request):
    postrentsale = PostRentSale.objects.filter(type_property='1', rent_sale='1').order_by('-id')
    paginator = Paginator(postrentsale, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    postrentsale = paginator.get_page(page_number)

    context = {
        'postrentsale': postrentsale
    }
    return render(request, 'pages/objpage.html', context)


# Аренда - Квартиры
def arenda_kv_page(request):
    postrentsale = PostRentSale.objects.filter(type_property='2', rent_sale='1').order_by('-id')
    paginator = Paginator(postrentsale, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    postrentsale = paginator.get_page(page_number)

    context = {
        'postrentsale': postrentsale
    }
    return render(request, 'pages/objpage.html', context)


# Аренда - Участки
def arenda_uchactky_page(request):
    postrentsale = PostRentSale.objects.filter(type_property='3', rent_sale='1').order_by('-id')
    paginator = Paginator(postrentsale, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    postrentsale = paginator.get_page(page_number)

    context = {
        'postrentsale': postrentsale
    }
    return render(request, 'pages/objpage.html', context)


# Аренда - Коммерческая недвижимость
def arenda_com_ned_page(request):
    postrentsale = PostRentSale.objects.filter(type_property='4', rent_sale='1').order_by('-id')
    paginator = Paginator(postrentsale, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    postrentsale = paginator.get_page(page_number)

    context = {
        'postrentsale': postrentsale
    }
    return render(request, 'pages/objpage.html', context)


# Продажа - Дома
def sale_dom_page(request):
    postrentsale = PostRentSale.objects.filter(type_property='1', rent_sale='2').order_by('-id')
    paginator = Paginator(postrentsale, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    postrentsale = paginator.get_page(page_number)

    context = {
        'postrentsale': postrentsale
    }
    return render(request, 'pages/objpage.html', context)


# Продажа - Квартиры
def sale_kv_page(request):
    postrentsale = PostRentSale.objects.filter(type_property='2', rent_sale='2').order_by('-id')
    paginator = Paginator(postrentsale, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    postrentsale = paginator.get_page(page_number)

    context = {
        'postrentsale': postrentsale
    }
    return render(request, 'pages/objpage.html', context)


# Продажа - Участки
def sale_uchactky_page(request):
    postrentsale = PostRentSale.objects.filter(type_property='3', rent_sale='2').order_by('-id')
    paginator = Paginator(postrentsale, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    postrentsale = paginator.get_page(page_number)

    context = {
        'postrentsale': postrentsale
    }
    return render(request, 'pages/objpage.html', context)


# Продажа - Коммерческая недвижимость
def sale_com_ned_page(request):
    postrentsale = PostRentSale.objects.filter(type_property='4', rent_sale='2').order_by('-id')
    paginator = Paginator(postrentsale, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    postrentsale = paginator.get_page(page_number)

    context = {
        'postrentsale': postrentsale
    }
    return render(request, 'pages/objpage.html', context)


# Дома
def dom_page(request):
    postrentsale = PostRentSale.objects.filter(type_property='1').order_by('-id')
    paginator = Paginator(postrentsale, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    postrentsale = paginator.get_page(page_number)

    context = {
        'postrentsale': postrentsale
    }
    return render(request, 'pages/objpage_all.html', context)


# Квартиры
def kv_page(request):
    postrentsale = PostRentSale.objects.filter(type_property='2').order_by('-id')
    paginator = Paginator(postrentsale, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    postrentsale = paginator.get_page(page_number)

    context = {
        'postrentsale': postrentsale
    }
    return render(request, 'pages/objpage_all.html', context)


# Участки
def uchactky_page(request):
    postrentsale = PostRentSale.objects.filter(type_property='3').order_by('-id')
    paginator = Paginator(postrentsale, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    postrentsale = paginator.get_page(page_number)

    context = {
        'postrentsale': postrentsale
    }
    return render(request, 'pages/objpage_all.html', context)


# Коммерческая недвижимость
def com_ned_page(request):
    postrentsale = PostRentSale.objects.filter(type_property='4').order_by('-id')
    paginator = Paginator(postrentsale, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    postrentsale = paginator.get_page(page_number)

    context = {
        'postrentsale': postrentsale
    }
    return render(request, 'pages/objpage_all.html', context)


# Отзывы
def reviews(request):
    reviews = Reviews.objects.all()
    context = {
        'reviews': reviews,
    }
    page="reviews"
    return render(request, 'pages/reviews.html', context)


# ОТдельная стр Отзывов
class ReviewsDetailView(View):
    def get(self, request, slug):
        reviews = Reviews.objects.get(slug=slug)
        context = {
            'reviews': reviews,
        }
        page="reviews"
        return render(request, "pages/reviews_detail.html", context)


# Все Объекты
def objects_all(request):
    postrentsale = PostRentSale.objects.all()
    paginator = Paginator(postrentsale, 8) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'pages/objects_all.html', {'page_obj': page_obj})


# О компании
def about(request):
    page="about"
    return render(request, 'pages/about.html')


# Услуги
def services(request):
    page="services"
    return render(request, 'pages/services.html')


# ХОЧУ ПРОДАТЬ
def want_sell(request):
    page="want_sell"
    form = ContactForm(request.POST)
    return render(request, 'pages/want_sell.html', {'form':form, 'page':page})


# Проекты
def projects(request):
    page="projects"
    return render(request, 'pages/projects.html')


def error_404(request, exception):
    return render(request, 'pages/404.html', status=404)