from django import forms
from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, HttpRequest, Http404, HttpResponse, FileResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from django.core import serializers
from django.urls import reverse, path
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from passlib.hash import pbkdf2_sha256
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.template.loader import get_template
from django.contrib.auth.models import User
from django.conf import settings
from django.db import IntegrityError
from django.template import Context, loader
from django.db.models import Count, Exists, Q
from datetime import datetime, date
from django.contrib.auth.hashers import check_password

#biblioteca para cria PDF
import random, json, re, os, sweetify, reportlab, qrcode, copy, urllib
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Line
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch, mm
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, B4, cm, letter, landscape
from reportlab.platypus import (Image, PageBegin, PageBreak, Paragraph, Table,tables, TableStyle, SimpleDocTemplate,
 Spacer, NextPageTemplate, Frame, PageTemplate)
from reportlab.rl_config import defaultPageSize
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics, ttfonts

#biblioteca para world docx
from docx import Document
import docx
from docx.shared import Inches, Length, Pt, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_TAB_ALIGNMENT, WD_TAB_LEADER,WD_UNDERLINE
from docx.enum.style import WD_STYLE_TYPE, WD_STYLE
from docx.enum.table import WD_ALIGN_VERTICAL, WD_TABLE_ALIGNMENT, WD_ROW_HEIGHT, WD_ROW_HEIGHT_RULE
from docx.enum.section import WD_ORIENT, WD_SECTION
from docx.text.run import Font, Run
from docx.dml.color import ColorFormat
from SOFIL_RH.settings import  MEDIA_ROOT, MEDIA_URL, SENHA_PADRAO, DATA_MES, DATA_ANO, DATE_FORMAT

#CORE HELP MODULO DE AJUDA
from core_help.opcoes_escolha import GENERO, ESTADO_CIVIL, GRAU_PAGAMENTO, TIPO_DECLARACAO, MESES
from core_help.models import Cursos, Semestre, Ano, Especialidade, Descricao_Nota, Municipio
from core_help.validar import validar_cadeira_atraso, validar_nota_final_monografia

# SECRETARIA
from secretaria.models import (Pessoa, Estudante, Profissao, Modulo_Disciplina, Gerar_Numero_Matricula, Matricula, Monografia, Nota, Nota_final_Monografia, Estudante_Curso,
Chaves_Modulo_Curso)

from secretaria.forms import (PessoaForm, EstudanteForm, ProfissaoForm, Modulo_MestradoForm, MonografiaForm, Nota_lancamento_Form, Consultar_alterar_pessoaForm, Gerar_numeroEstudante_Form, Matricula_Form, Emitir_declaracao_ConsultarDados_Form, Modulo_PosGraduacaoForm, Menu_listagem_Form, Nota_final_Monografia_Form, Chaves_Modulo_Curso_Form,
    consultar_dados_pessoal_Form, Associar_Modulo_Form)

# FINANÇAS
from financas.models import Pagamento
from financas.forms import PagamentoForm, Listar_PagamentoForm

#UTILIZADOR
from utilizador.models import Controla_SenhaPadrao
from utilizador.forms import Utilizador_Form, LoginForm, Troca_SenhaPadrao_Form, Actualizar_categoria_Form
