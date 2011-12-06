# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.utils.translation import ugettext as _
from django.core.paginator import Paginator
from models import ContaPagar, ContaReceber, CONTA_STATUS_APAGAR
from forms import FormPagamento
import datetime

def contas(request):
    contas_a_pagar = ContaPagar.objects.filter(
        status=CONTA_STATUS_APAGAR,
    )
    contas_a_receber = ContaReceber.objects.filter(
        status=CONTA_STATUS_APAGAR,
    )
    return render_to_response('contas/contas.html',locals(), context_instance=RequestContext(request),  )

def conta(request, conta_id, classe):
    conta = get_object_or_404(classe, id=conta_id)
    form_pagamento = FormPagamento()
    return render_to_response( 'contas/conta.html', locals(), context_instance=RequestContext(request),  )

def conta_pagamento(request, conta_id, classe):
    conta = get_object_or_404(classe, id=conta_id)
    if request.method == 'POST':
        form_pagamento = FormPagamento(request.POST)
      
        if form_pagamento.is_valid():
            form_pagamento.salvar_pagamento(conta)
    
    return HttpResponseRedirect(request.META['HTTP_REFERER'])


def contas_por_classe(request, classe, titulo):
    contas = classe.objects.order_by('status','data_vencimento')
    paginacao = Paginator(contas, 2)
    pagina = paginacao.page(request.GET.get('pagina',1))
    titulo = _(titulo)
    return render_to_response( 'contas/contas_por_classe.html', locals(),context_instance=RequestContext(request), )

#def editar_conta(request, classe_form, titulo, conta_id = None):
#    form = classe_form()

#    return render_to_response( 'contas/editar_conta.html', locals(), context_instance= RequestContext(request),)

def editar_conta(request, classe_form, titulo, conta_id=None):
    if conta_id:
        conta = get_object_or_404( classe_form._meta.model,id=conta_id )
    else:
        conta = None
    
    if request.method == 'POST':
        formu = classe_form(request.POST, instance=conta)
        if formu.is_valid():
            conta = formu.save(commit=False)
            conta.usuario = request.user
            conta.save()
            return HttpResponseRedirect(conta.get_absolute_url())
    else:
        formu = classe_form( initial ={'data_vencimento': datetime.date.today() }, instance=conta, )


    return render_to_response( 'contas/editar_conta.html', locals(),context_instance=RequestContext(request), )


def excluir_conta(request, classe, conta_id, proxima='/contas/'):
    conta = get_object_or_404(classe, id=conta_id)
    conta.delete()
    request.user.message_set.create(
        message='Conta excluida com sucesso!'
    )
    return HttpResponseRedirect(proxima)


