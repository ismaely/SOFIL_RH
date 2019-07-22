from django.urls import path
from . import views


app_name = 'secretaria'
urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('registar_cadastro/', views.registar_cadastro, name='registar-cadastro'),
    path('registar_modulo/', views.registar_modulo_mestrado, name='registar-modulo-mestrado'),
    path('registar_posGraduacao/', views.registar_modulo_posGraduacao, name='registar-modulo-posGraduacao'),
    path('registar_monografia/', views.registar_Monografia, name='registar-monografia'),
    path('confirma_matricula/', views.registar_confirma_matricula, name='confirma-matricula'),
    path('listar_dados_estudante/', views.listar_dados_estudante, name='listar-dados-estudante'),
    path('listar_modulos_mestrado/', views.listar_modulos_mestrado, name='listar-modulos-mestrado'),
    path('listar_modulos_posgraduacao/', views.listar_modulos_posGraduacao, name='listar-modulos-posgraduacao'),
    path('atrbuir_numero_estudante/', views.gerar_numeroEstudante, name='atrbuir-estudante'),
    path('listar_monografia_mestrado/', views.listar_monografia_mestrado, name='listar-monografia-mestrado'),
    path('listar_monografia_posGraduacao/', views.listar_monografia_posGraduacao, name='listar-monografia-posGraduacao'),
    path('emitir_delaracao/', views.emitir_delaracao, name='emitir-delaracao'),
    path('lancamento_nota/', views.lancamento_nota, name='lancamento-nota'),
    path('recebe_id_curso_ajax/', views.recebe_id_curso_ajax, name='recebe-id-curso-ajax'),
    path('registar_nota_estudante/', views.registar_nota_ajax, name='registar-nota-estudante'),
]
