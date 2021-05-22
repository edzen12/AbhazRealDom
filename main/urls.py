from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    index, reviews, about, projects, services, want_sell,
    ReviewsDetailView, PostRentSaleDetailView,
    arenda_dom_page, arenda_kv_page, arenda_uchactky_page, arenda_com_ned_page,
    sale_dom_page, sale_kv_page, sale_uchactky_page, sale_com_ned_page,
    dom_page, kv_page, uchactky_page, com_ned_page,
)

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('projects/', projects, name='projects'),
    path('reviews/', reviews, name='reviews'),
    path('services/', services, name='services'),
    path('want-sell/', want_sell, name='want_sell'),

    path('arenda-dom-page/', arenda_dom_page, name='arenda_dom_page'),
    path('arenda-kv-page/', arenda_kv_page, name='arenda_kv_page'),
    path('arenda-uchactky-page/', arenda_uchactky_page, name='arenda_uchactky_page'),
    path('arenda-comned-page/', arenda_com_ned_page, name='arenda_com_ned_page'),

    path('sale-dom-page/', sale_dom_page, name='sale_dom_page'),
    path('sale-kv-page/', sale_kv_page, name='sale_kv_page'),
    path('sale-uchactky-page/', sale_uchactky_page, name='sale_uchactky_page'),
    path('sale-comned-page/', sale_com_ned_page, name='sale_com_ned_page'),

    path('dom-page/', dom_page, name='dom_page'),
    path('kv-page/', kv_page, name='kv_page'),
    path('uchactky-page/', uchactky_page, name='uchactky_page'),
    path('comned-page/', com_ned_page, name='com_ned_page'),

    path('reviews/<slug:slug>/', ReviewsDetailView.as_view(), name="reviews_detail"),
    path('postrentsale/<slug:slug>/', PostRentSaleDetailView.as_view(), name="postrentsale_detail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
