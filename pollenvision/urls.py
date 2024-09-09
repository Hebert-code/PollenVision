from django.urls import path
from pollenvision.views import index

urlpatterns = [
    path('', index, name='index')
]