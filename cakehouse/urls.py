from django.urls import path 
from . import  views  

urlpatterns = [

        path('', views.index, name='index'),
        path('Ver_productos', views.Ver_productos, name='Ver_productos'),
        path('Inicio_sesion', views.Inicio_sesion, name='Inicio_sesion'),
        path('Registro', views.Registro, name='Registro'),

]