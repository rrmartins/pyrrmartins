from django.conf.urls.defaults import *
from models import ContaPagar, ContaReceber

urlpatterns = patterns('contas.views',
    url('^$', 'contas', name='contas'),
    url('^pagar/(?P<conta_id>\d+)/$', 'conta', {'classe': ContaPagar},
         name='conta_a_pagar'),
    url('^receber/(?P<conta_id>\d+)/$', 'conta', {'classe':
         ContaReceber}, name='conta_a_receber'),
    url('^pagar/(?P<conta_id>\d+)/pagar/$', 'conta_pagamento',
            {'classe': ContaPagar},
            name='conta_a_pagar_pagamento'),
    url('^receber/(?P<conta_id>\d+)/pagar/$', 'conta_pagamento',
            {'classe': ContaReceber},
            name='conta_a_receber_pagamento'),
    url('^pagar/$', 'contas_por_classe',
            {'classe': ContaPagar, 'titulo': 'Contas a Pagar'},
            name='contas_a_pagar'),
    url('^receber/$', 'contas_por_classe',
            {'classe': ContaReceber, 'titulo': 'Contas a Receber'},
            name='contas_a_receber'),

)
