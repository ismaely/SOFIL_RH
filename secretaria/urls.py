from django.urls import path, re_path
from . import views


app_name = 'secretaria'
urlpatterns = [
    #path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('registar_cadastro/', views.registar_cadastro, name='registar-cadastro'),
    path('registar_modulo/', views.registar_modulo_mestrado, name='registar-modulo-mestrado'),
    path('registar_posGraduacao/', views.registar_modulo_posGraduacao, name='registar-modulo-posGraduacao'),
    path('registar_monografia/', views.registar_Monografia, name='registar-monografia'),
    path('confirma_matricula/', views.registar_confirma_matricula, name='confirma-matricula'),
    path('listar_dados_nominal/', views.listar_dados_nominal, name='listar-dados-nominal'),
    path('listar_modulos_mestrado/', views.listar_modulos_mestrado, name='listar-modulos-mestrado'),
    path('listar_modulos_posgraduacao/', views.listar_modulos_posGraduacao, name='listar-modulos-posgraduacao'),
    path('atrbuir_numero_estudante/', views.gerar_numeroEstudante, name='atrbuir-estudante'),
    path('listar_monografia_mestrado/', views.listar_monografia_mestrado, name='listar-monografia-mestrado'),
    path('listar_monografia_posGraduacao/', views.listar_monografia_posGraduacao, name='listar-monografia-posGraduacao'),
    path('emitir_delaracao/', views.emitir_delaracao, name='emitir-delaracao'),
    path('gerar_lista_estudante_pdf/', views.gerar_lista_estudante_pdf, name='lista-estudante-pdf'),
    path('lancamento_nota/', views.lancamento_nota, name='lancamento-nota'),
    path('recebe_id_curso_ajax/', views.recebe_id_curso_ajax, name='recebe-id-curso-ajax'),
    path('recebe_ano_retornaSemestre_ajax/', views.recebe_ano_retornaSemestre_ajax, name='recebe-ano-semestre-ajax'),
    path('recebe_idCurso_retornaEspecialidadeModuloAno_ajax/', views.recebe_idCurso_retornaEspecialidadeModuloAno_ajax, name='dCurso-retornaEspecialidade-ajax'),
    path('recebe_grau_academico_ajax/', views.recebe_grau_academico_ajax, name='recebe-grau-ajax'),
    path('imprimir_ficha_matricula/<int:id_value>/', views.imprimir_ficha_matricula, name='imprimir-ficha-matricula'),
    path('consultar_dados_pessoal/', views.consultar_dados_pessoal, name='consultar-dados-pessoal'),
    #path(r'^imprimir_ficha_matricula/(?P<id_value>\s+)/?$', views.imprimir_ficha_matricula, name='imprimir-ficha-matricula'),
]
 