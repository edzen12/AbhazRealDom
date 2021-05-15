from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import City, RSObjects, ImageShots


def index(request):
    city = City.objects.all()
    rs_objects = RSObjects.objects.all()
    context = {
        'city': city,
        'rs_objects': rs_objects,
    }
    return render(request, 'index.html', context)
