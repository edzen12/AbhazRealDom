from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    index, reviews, about, projects,
    ReviewsDetailView, PostRentSaleDetailView
)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('reviews/', reviews, name='reviews'),
    path('reviews/<slug:slug>/', ReviewsDetailView.as_view(), name="reviews_detail"),
    path('postrentsale/<slug:slug>/', PostRentSaleDetailView.as_view(), name="postrentsale_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
