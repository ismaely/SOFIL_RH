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

import sweetify
from core_help.opcoes_escolha import GENERO, ESTADO_CIVIL

from secretaria.models import Pessoa, Estudante, Profissao
from secretaria.forms import PessoaForm, EstudanteForm, ProfissaoForm, Modulo_DisciplinaForm
