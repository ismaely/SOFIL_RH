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
    path('listar_estudantes_matriculados/', views.listar_estudantes_matriculados, name='estudantes-matriculados'),
    path('listar_modulos_mestrado/', views.listar_modulos_mestrado, name='listar-modulos-mestrado'),
    path('listar_modulos_posgraduacao/', views.listar_modulos_posGraduacao, name='listar-modulos-posgraduacao'),
    path('atrbuir_numero_estudante/', views.gerar_numeroEstudante, name='atrbuir-estudante'),
    path('emitir_delaracao/', views.emitir_delaracao, name='emitir-delaracao'),
    path('gerar_lista_estudante_pdf/', views.gerar_lista_estudante_pdf, name='lista-estudante-pdf'),
    path('lancamento_nota/', views.lancamento_nota, name='lancamento-nota'),
    path('recebe_id_curso_ajax/', views.recebe_id_curso_ajax, name='recebe-id-curso-ajax'),
    path('recebe_ano_retornaSemestre_ajax/', views.recebe_ano_retornaSemestre_ajax, name='recebe-ano-semestre-ajax'),
    path('recebe_idCurso_retornaEspecialidade_ajax/', views.recebe_idCurso_retornaEspecialidadeModuloAno_ajax, name='dCurso-retornaEspecialidade-ajax'),
    path('recebe_grau_academico_ajax/', views.recebe_grau_academico_ajax, name='recebe-grau-ajax'),
    path('recebe_naturalidade_retorna_municipio_ajax/', views.recebe_naturalidade_retorna_municipio_ajax, name='naturalidade_retorna_municipio'),
    path('imprimir_ficha_matricula/<int:id_value>/', views.imprimir_ficha_matricula, name='imprimir-ficha-matricula'),
    path('consultar_dados_pessoal/', views.consultar_dados_pessoal, name='consultar-dados-pessoal'),
    path('consultar_dados_cadastro_pessoa/', views.consultar_dados_cadastro_pessoa, name='consultar-dados-cadastro'),
    
    path('registar_nota_final_monografia/', views.registar_nota_final_monografia, name='nota_final'),
    path('listar_monografias/', views.listar_monografias, name='monografia'),
    path('eliminar_monografias/<int:pk>/', views.eliminar_monografia, name='eliminar-monografia'),
    path('ativar_modulo_mestrado/<int:pk>/', views.ativar_modulo_mestrado, name='ativar_modulo_mestrado'),
    path('cancelar_modulo_mestrado/<int:pk>/', views.cancelar_modulo_mestrado, name='cancelar_modulo_mestrado'),

    path('ativar_modulo_posGraduacao/<int:pk>/', views.ativar_modulo_posGraduacao, name='ativar-modulo-posGraduacao'),
    path('cancelar_modulo_posGraduacao/<int:pk>/', views.cancelar_modulo_posGraduacao, name='cancelar-modulo-posGraduacao'),
    path('editar_modulo_mestrado/<int:pk>/', views.editar_modulo_mestrado, name='editar-modulo-mestrado'),
    path('editar_modulo_posGraduacao/<int:pk>/', views.editar_modulo_posGraduacao, name='editar-modulo-posGraduacao'),
    path('editar_monografias/<int:pk>/', views.editar_monografias, name='editar-monografias'),
    path('ativar_aprovacao_monografia/<int:pk>/', views.ativar_aprovacao_monografia, name='aprovacao-monografia'),
    path('cancelar_monografia/<int:pk>/', views.cancelar_monografia, name='cancelar-monografia'),
    path('editar_registar_cadastro/<int:pk>/', views.editar_registar_cadastro, name='editar-cadastro'),
    path('editar_confirma_matricula/<int:pk>/', views.editar_confirma_matricula, name='editar-matricula'),
]
