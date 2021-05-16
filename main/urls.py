from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import index, reviews, about, projects


urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('reviews/', reviews, name='reviews'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
