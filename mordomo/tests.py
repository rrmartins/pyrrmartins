import datetime
from django.test import TestCase
from django.contrib.auth.models import User
from contas.models import Pessoa, Historico, ContaPagar, CONTA_STATUS_APAGAR, CONTA_STATUS_PAGO

class MordomoTest(TestCase):
    def setUp(self):
        self.usuario, novo = User.objects.get_or_create( username = 'admin' )
        self.pessoa, novo = Pessoa.objects.get_or_create( usuario = self.usuario, nome = 'Rodrigo Martins', )
        self.historico, novo = Historico.objects.get_or_create( usuario = self.usuario, descricao = 'Agua', )

    def tearDown(self):
        pass

    def testUmMaisUm(self):
        self.assertEquals(1+1, 2)

    def testObjetosCriados(self):
        self.assertEquals(User.objects.count(), 1)
        self.assertEquals(Pessoa.objects.count(), 1)
        self.assertEquals(Historico.objects.count(), 1)

    def testContasPendentes(self):
        from mordomo.models import obter_contas_pendentes

        for numero in (-50, 50):
            if numero % 2:
                novo_status = CONTA_STATUS_APAGAR
            else:
                novo_status = CONTA_STATUS_PAGO
            
            nova_data = datetime.date.today() + datetime.timedelta(days=numero)

            novo_valor = numero + 70
