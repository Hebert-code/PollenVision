from django.urls import path
from pollenvision.views import index, dashboard, upload, resultado, historico, relatorios, suporte

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('upload/', upload, name='upload'),
    path('resultado/', resultado, name='resultado'),
    path('historico/', historico, name='historico'),
    path('relatorios/', relatorios, name='relatorios'),
    path('suporte/', suporte, name='suporte')
]