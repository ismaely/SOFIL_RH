from django.urls import path
from . import views

app_name = 'secretaria'
urlpatterns = [
    path('', views.Home_View.as_view(), name='home'),
    path('home/', views.Home_View.as_view(), name='home-kanguitu'),
    path('login/', views.login, name='login'),
    path('registar_cadastro/', views.Registar_cadastro, name='registar-cadastro'),
    path('retorna_municipio/', views.retorna_municipio, name='retorna-municipio'),
    #path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    #path('<int:question_id>/vote/', views.vote, name='vote'),
]
