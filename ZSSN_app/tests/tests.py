from urllib import response
from django.test import TestCase
from ..models import Inventario, Sobrevivente
from ..forms import SobreviventeForm
from http import HTTPStatus



class SobreviventeTestCase(TestCase):

    def setUp(self):
        p1 = Sobrevivente.objects.create(
            nome = 'Teste1',
            idade = 23,
            sexo = 'F', 
            log = 0,
            lat = 0,
        )

        p2 = Sobrevivente.objects.create(
            nome = 'Teste2',
            idade = 25,
            sexo = 'M', 
            log = 0,
            lat = 0,
        )

        i1 = Inventario.objects.create(
            agua = 2,
            alimento = 3,
            medicacao = 4,
            municao = 5,
            sobrevivente = p1
        )

        i2= Inventario.objects.create(
            agua = 2,
            alimento = 3,
            medicacao = 4,
            municao = 5,
            sobrevivente = p2
        )


    def test_view_url(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
        p1 = Sobrevivente.objects.get(nome='Teste1')
        response = self.client.get('/edit/'+str(p1.id))
        self.assertEqual(response.status_code, HTTPStatus.OK)
       
        p2 = Sobrevivente.objects.get(nome='Teste2')
        response = self.client.get('/trocar_itens/'+str(p1.id)+'/'+str(p2.id))
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.client.get('/acusar/'+str(p1.id)+'/'+str(p2.id))
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.client.get('/api/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.client.get('/api/Sobreviventes/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

        response = self.client.get('/api/Inventarios/')
        self.assertEqual(response.status_code, HTTPStatus.OK)






  
  


      
     


        




      


