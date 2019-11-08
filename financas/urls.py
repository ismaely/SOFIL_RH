# urls.py
# @Author : Gunza Ismael (7ilipe@gmail.com)
# @Link   : 
# @Date   : 27/06/2019, 08:55:23
from django.urls import path
from . import views

app_name = 'financas'
urlpatterns = [
    path('registar_pagamento/', views.registar_Pagamento, name='registar-pagamento'),
    path('listar_pagamento/', views.listar_pagamento, name='listar-pagamento'),
    path('listar_divida/', views.listar_dividas, name='listar-divida'),
    path('imprmir_fatura_pagamento/<int:id>/', views.imprmir_fatura_pagamento, name='imprmir_fatura'),
    
]
