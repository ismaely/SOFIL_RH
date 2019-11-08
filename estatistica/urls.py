from django.urls import path, re_path
from . import views


app_name = 'estatistica'
urlpatterns = [
    path('menu_geral_mestrado/', views.menu_geral_mestrado, name='menu-mestrado'),
   # path('registar_modulo/', views.registar_modulo_mestrado, name='registar-modulo-mestrado'),
   
]
