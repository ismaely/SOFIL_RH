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

import sweetify
from core_help.opcoes_escolha import GENERO, ESTADO_CIVIL, GRAU_PAGAMENTO
from core_help.models import Cursos

# SECRETARIA
from secretaria.models import Pessoa, Estudante, Profissao, Modulo_Disciplina
from secretaria.forms import (PessoaForm, EstudanteForm, ProfissaoForm, Modulo_DisciplinaForm, MonografiaForm)

# FINANÇAS
from financas.models import Pagamento
from financas.forms import PagamentoForm


#UTILIZADOR
from utilizador.models import Controla_SenhaPadrao
from utilizador.forms import Utilizador_Form, LoginForm, Troca_SenhaPadrao_Form


SENHA_PADRAO = "cpppgl"