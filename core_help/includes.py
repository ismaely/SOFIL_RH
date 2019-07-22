from django import forms
from django.forms import ModelForm
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, JsonResponse, HttpRequest, Http404, HttpResponse, FileResponse
from django.core.exceptions import ObjectDoesNotExist
from django.core.serializers import serialize
from django.core import serializers
from django.urls import reverse
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
from django.db.models import Count

#biblioteca para cria PDF
import random, json, re, os, sweetify
from io import BytesIO
import reportlab
from reportlab.pdfgen import canvas
from reportlab.graphics.shapes import Drawing, Line
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.utils import ImageReader
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4, cm, letter, landscape
from reportlab.platypus import (Image, PageBegin, PageBreak, Paragraph, Table, TableStyle, SimpleDocTemplate,
 Spacer, NextPageTemplate, Frame, PageTemplate)
from reportlab.rl_config import defaultPageSize
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT, TA_RIGHT
from django.urls import path

from SOFIL_RH.settings import  MEDIA_ROOT, MEDIA_URL, SENHA_PADRAO

#CORE HELP MODULO DE AJUDA
from core_help.opcoes_escolha import GENERO, ESTADO_CIVIL, GRAU_PAGAMENTO
from core_help.models import Cursos
# SECRETARIA
from secretaria.models import Pessoa, Estudante, Profissao, Modulo_Disciplina, Gerar_Numero_Matricula, Matricula, Monografia, Nota
from secretaria.forms import (PessoaForm, EstudanteForm, ProfissaoForm, Modulo_MestradoForm, MonografiaForm, Nota_lancamento_Form,
 Gerar_numeroEstudante_Form, Matricula_Form, Emitir_declaracao_Form, Modulo_PosGraduacaoForm)

# FINANÇAS
from financas.models import Pagamento
from financas.forms import PagamentoForm


#UTILIZADOR
from utilizador.models import Controla_SenhaPadrao
from utilizador.forms import Utilizador_Form, LoginForm, Troca_SenhaPadrao_Form


