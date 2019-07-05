from django.urls import path
from . import views


app_name = 'secretaria'
urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home, name='home'),
    path('registar_cadastro', views.registar_cadastro, name='registar-cadastro'),
    path('registar_modulo', views.registar_modulo, name='registar-modulo'),
    path('registar_monografia', views.registar_Monografia, name='registar-monografia'),
    path('confirma_matricula', views.registar_confirma_matricula, name='confirma-matricula'),
    path('listar_dados_estudante', views.listar_dados_estudante, name='listar-dados-estudante'),
    path('registar_docente_funcionario', views.registar_docente_funcionario, name='registar-funcionario'),
    path('listar_modulos', views.listar_modulos, name='listar-modulos'),
]
