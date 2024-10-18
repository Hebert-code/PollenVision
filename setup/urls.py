from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('home.urls')), #home page
    path('admin/', admin.site.urls),
    path('pollenvision/', include('pollenvision.urls')),
    path('accounts/', include('allauth.urls')),
]
