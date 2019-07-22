#
# urls.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   : 
# @Date   : 09/07/2019, 06:09:56
from django.urls import path
from . import views


app_name = 'utilizador'
urlpatterns = [
    #path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('accounts/login/', views.login, name='login'),
    path('sair/', views.sair, name='sair'),
    path('registar_utilizador/', views.registar_utilizador, name='registar-utilizador'),
    path('troca_padrao/', views.troca_senha_padrao, name='troca-senha-padrao'),
   
]
