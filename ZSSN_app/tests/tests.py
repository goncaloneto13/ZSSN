from django.test import TestCase
from ..models import Inventario, Sobrevivente

class SobreviventeTestCase(TestCase):

    def setUp(self):
        p1 = Sobrevivente.objects.create(
            nome = 'Teste1',
            idade = 23,
            sexo = 'F', 
            log = 0,
            lat = 0,
        )

        Inventario.objects.create(
            agua = 2,
            alimento = 3,
            medicacao = 4,
            municao = 5,
            sobrevivente = p1
        )

        

    def test_retorno_str(self):

        p1 = Sobrevivente.objects.get(nome='Teste1')
        self.assertEquals(p1.__str__(),'Teste1')

    def test_troca_itens(self):




      


