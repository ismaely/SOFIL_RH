from django.urls import path, re_path
from hashlib import blake2b
from . import views

# blake2b(b'registar_posGraduacao').hexdigest()+'/'

app_name = 'secretaria'
urlpatterns = [
    #path('', views.home, name='home'),
    path(blake2b(b'home').hexdigest()+'/', views.home, name='home'),
    path(blake2b(b'registar_cadastro').hexdigest()+'/', views.registar_cadastro, name='registar-cadastro'),
    path(blake2b(b'registar_modulo').hexdigest()+'/', views.registar_modulo_mestrado, name='registar-modulo-mestrado'),
    path(blake2b(b'registar_posGraduacao').hexdigest()+'/', views.registar_modulo_posGraduacao, name='registar-modulo-posGraduacao'),
    path(blake2b(b'registar_monografia').hexdigest()+'/', views.registar_Monografia, name='registar-monografia'),
    path(blake2b(b'confirma_matricula').hexdigest()+'/', views.registar_confirma_matricula, name='confirma-matricula'),
    path(blake2b(b'listar_estudantes_matriculados').hexdigest()+'/', views.listar_estudantes_matriculados, name='estudantes-matriculados'),
    path(blake2b(b'listar_modulos_mestrado').hexdigest()+'/', views.listar_modulos_mestrado, name='listar-modulos-mestrado'),
    path(blake2b(b'listar_modulos_posgraduacao').hexdigest()+'/', views.listar_modulos_posGraduacao, name='listar-modulos-posgraduacao'),
    path(blake2b(b'atrbuir_numero_estudante').hexdigest()+'/', views.gerar_numeroEstudante, name='atrbuir-estudante'),
    
    path(blake2b(b'gerar_lista_estudante_pdf').hexdigest()+'/', views.gerar_lista_estudante_pdf, name='lista-estudante-pdf'),
    path(blake2b(b'lancamento_nota').hexdigest()+'/', views.lancamento_nota, name='lancamento-nota'),
    path('recebe_id_curso_ajax/', views.recebe_id_curso_ajax, name='recebe-id-curso-ajax'),
    path('recebe_ano_retornaSemestre_ajax/', views.recebe_ano_retornaSemestre_ajax, name='recebe-ano-semestre-ajax'),
    path('recebe_idCurso_retornaEspecialidade_ajax/', views.recebe_idCurso_retornaEspecialidadeModuloAno_ajax, name='dCurso-retornaEspecialidade-ajax'),
    path('recebe_grau_academico_ajax/', views.recebe_grau_academico_ajax, name='recebe-grau-ajax'),
    path('recebe_naturalidade_retorna_municipio_ajax/', views.recebe_naturalidade_retorna_municipio_ajax, name='naturalidade_retorna_municipio'),
    path(blake2b(b'imprimir_ficha_matricula').hexdigest()+'/<int:pk>/<int:value>/', views.imprimir_ficha_matricula, name='imprimir-ficha-matricula'),
    path(blake2b(b'consultar_dados_pessoal').hexdigest()+'/', views.consultar_dados_pessoal, name='consultar-dados-pessoal'),
    path(blake2b(b'consultar_dados_cadastro_pessoa').hexdigest()+'/', views.consultar_dados_cadastro_pessoa, name='consultar-dados-cadastro'),
    path(blake2b(b'registar_nota_final_monografia').hexdigest()+'/', views.registar_nota_final_monografia, name='nota_final'),
    path(blake2b(b'listar_monografias').hexdigest()+'/', views.listar_monografias, name='monografia'),
    path(blake2b(b'eliminar_monografias').hexdigest()+'/<int:pk>/', views.eliminar_monografia, name='eliminar-monografia'),
    path(blake2b(b'ativar_modulo_mestrado').hexdigest()+'/<int:pk>/', views.ativar_modulo_mestrado, name='ativar_modulo_mestrado'),
    path(blake2b(b'cancelar_modulo_mestrado').hexdigest()+'/<int:pk>/', views.cancelar_modulo_mestrado, name='cancelar_modulo_mestrado'),

    path(blake2b(b'ativar_modulo_posGraduacao').hexdigest()+'/<int:pk>/', views.ativar_modulo_posGraduacao, name='ativar-modulo-posGraduacao'),
    path(blake2b(b'cancelar_modulo_posGraduacao').hexdigest()+'/<int:pk>/', views.cancelar_modulo_posGraduacao, name='cancelar-modulo-posGraduacao'),
    path(blake2b(b'editar_modulo_mestrado').hexdigest()+'/<int:pk>/', views.editar_modulo_mestrado, name='editar-modulo-mestrado'),
    path(blake2b(b'editar_modulo_posGraduacao').hexdigest()+'/<int:pk>/', views.editar_modulo_posGraduacao, name='editar-modulo-posGraduacao'),
    path(blake2b(b'editar_monografias').hexdigest()+'/<int:pk>/', views.editar_monografias, name='editar-monografias'),
    path(blake2b(b'ativar_aprovacao_monografia').hexdigest()+'/<int:pk>/', views.ativar_aprovacao_monografia, name='aprovacao-monografia'),
    path(blake2b(b'cancelar_monografia').hexdigest()+'/<int:pk>/', views.cancelar_monografia, name='cancelar-monografia'),
    path(blake2b(b'editar_registar_cadastro').hexdigest()+'/<int:pk>/', views.editar_registar_cadastro, name='editar-cadastro'),
    path(blake2b(b'editar_confirma_matricula').hexdigest()+'/<int:pk>/', views.editar_confirma_matricula, name='editar-matricula'),
    path(blake2b(b'visualizar_monografia').hexdigest()+'/<int:pk>/', views.visualizar_monografia, name='visualizar-monografia'),
    path(blake2b(b'emitir_delaracao').hexdigest()+'/', views.emitir_delaracao, name='emitir-delaracao'),
    path(blake2b(b'emitir_delaracao_word').hexdigest()+'/', views.emitir_delaracao_word, name='emitir-declaracao-word'),
    path(blake2b(b'alterar_nota').hexdigest()+'/<int:pk>/', views.alterar_nota, name='alterar-nota'),
    path(blake2b(b'associar_modulo_existente').hexdigest()+'/', views.associar_modulo_existente, name='associar-modulo'),
]
