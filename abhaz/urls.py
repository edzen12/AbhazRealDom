from django.contrib import admin
from django.conf.urls import handler404
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('contanct/', include('contact.urls')),
]

handler404 = 'main.views.error_404'

