#
# urls.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   : 
# @Date   : 09/07/2019, 06:09:56
from django.urls import path
from . import views


app_name = 'utilizador'
urlpatterns = [
    path('', views.login_sistema, name='login'),
    path('login/', views.login_sistema, name='login'),
    path('accounts/login/', views.login_sistema, name='login'),
    path('sair/', views.sair, name='sair'),
    path('registar_utilizador/', views.registar_utilizador, name='registar-utilizador'),
    path('troca_padrao/', views.troca_senha_padrao, name='troca-senha-padrao'),
    path('criar_conta_utilizador/', views.criar_conta_utilizador, name='conta_utilizador'),
    path('listar_utilizador/', views.listar_utilizador, name='listar_utilizador'),
    path('desativar_conta/<int:pk>/', views.desativar_conta, name='desativar'),
    path('ativar_conta/<int:pk>/', views.ativar_conta, name='ativar'),
    path('atualizar_funcao_categoria/<int:pk>/', views.atualizar_funcao_categoria, name='atualizar_funcao'),
   
]
