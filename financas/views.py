from core_help.includes import *
from core_help.core import retorna_id

# Create your views here.



def listar_pagamento(request):
    lista =[]
    lista = Pagamento.objects.order_by('-id')
    context = {'lista': lista}
    return render(request, 'financa/listar_pagamentos.html', context)



def registar_Pagamento(request):
    form = PagamentoForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            pessoa = form.save(commit=False)
            pessoa.estudante_id = retorna_id(request.POST.get('estudante'))
            pessoa.save()
            sweetify.success(request, 'Pagamento Registado com sucesso!....', button='Ok', timer='3100')
            return HttpResponseRedirect(reverse('secretaria:home'))

    context = {'form':form,}
    return render (request, 'financa/registar_pagamento.html', context)
