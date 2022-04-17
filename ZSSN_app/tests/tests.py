from urllib import response
from django.test import TestCase
from ..models import Inventario, Sobrevivente
from http import HTTPStatus
from django.urls import reverse



class ZNNSTestCase(TestCase):

    def setUp(self):

      
        p1 = Sobrevivente.objects.create(
            nome = 'Teste1',
            data_n = "1994-09-12",
            sexo = 'F', 
            log = 0,
            lat = 0,
    
        )

        p2 = Sobrevivente.objects.create(
            nome = 'Teste2',
            data_n = "1998-08-13",
            sexo = 'M', 
            log = 0,
            lat = 0,

        )

        p3 = Sobrevivente.objects.create(
            nome = 'Teste3',
            data_n = "1998-08-13",
            sexo = 'M', 
            log = 0,
            lat = 0,
            infectado = True

        )

        i1 = Inventario.objects.create(
            agua = 100,
            alimentacao = 3,
            medicacao = 4,
            municao = 5,
            sobrevivente = p1
        )

        i2= Inventario.objects.create(
            agua = 3,
            alimentacao = 44,
            medicacao = 50,
            municao = 60,
            sobrevivente = p2
        )

        i3= Inventario.objects.create(
            agua = 32,
            alimentacao = 44,
            medicacao = 50,
            municao = 64,
            sobrevivente = p3
        )


    def test_view_url(self):
        response = self.client.get('/add/')
        self.assertEqual(response.status_code, HTTPStatus.OK)
    
    def test_view_url_edit(self): 
        p1 = Sobrevivente.objects.get(nome='Teste1')
        response = self.client.get('/edit/'+str(p1.id))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        
    def test_view_url_trocar_itens(self):   
        p1 = Sobrevivente.objects.get(nome='Teste1')
        p2 = Sobrevivente.objects.get(nome='Teste2')     
        response = self.client.get('/trocar_itens/'+str(p1.id)+'/'+str(p2.id))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_view_url_acusar(self):   
        p1 = Sobrevivente.objects.get(nome='Teste1')
        p2 = Sobrevivente.objects.get(nome='Teste2') 
        response = self.client.get('/acusar/'+str(p1.id)+'/'+str(p2.id))
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_view_url_api(self):   
        response = self.client.get('/api/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_view_url_api_sobreviventes(self):   
    
        response = self.client.get('/api/Sobreviventes/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_view_url_api_inventarios(self):   

        response = self.client.get('/api/Inventarios/')
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_view_uses_correct_template_add(self):
        response = self.client.get(reverse('add_sobreviventes'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ZSSN/add_sobreviventes.html')
        
    def test_view_uses_correct_template_and_context_edit(self):    

        p1 = Sobrevivente.objects.get(nome='Teste1')
    
        response = self.client.get(reverse('edit_sobrevivente', args=[p1.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ZSSN/edit_sobrevivente.html')    
        self.assertEqual(response.context['idade'], 27)
        self.assertEqual(response.context['sexo'],'Feminino')  
        #self.assertEqual(response.context['outros_sob'],Sobrevivente.objects.all())  

    def test_view_uses_correct_template_and_context_trocar_itens(self):     

        p1 = Sobrevivente.objects.get(nome='Teste1')
        p2 = Sobrevivente.objects.get(nome='Teste2')   

        response = self.client.get(reverse('trocar_itens', args=[p1.id, p2.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ZSSN/trocar_itens.html')
        self.assertTrue(response.context['qtd_itens0'] == [100,3,4,5])  
        self.assertTrue(response.context['qtd_itens1'] == [3,44,50,60])
        self.assertTrue(response.context['sobrevivente'] == p1)  
        self.assertTrue(response.context['outro_s'] == p2) 

    def test_view_uses_correct_template_and_context_acusar(self):       

        p1 = Sobrevivente.objects.get(nome='Teste1')
        p2 = Sobrevivente.objects.get(nome='Teste2') 

        response = self.client.get(reverse('acusar',args=[p1.id, p2.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ZSSN/acusar_infectado.html')    
        
    def test_relatorio_itens_medios(self):

        p1 = Sobrevivente.objects.get(nome='Teste1')
        p2 = Sobrevivente.objects.get(nome='Teste2') 
        p3 = Sobrevivente.objects.get(nome='Teste3') 

        response = self.client.get(reverse('relatorio'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'ZSSN/relatorio.html')
        self.assertEqual(response.context['agua'], 51)  
        self.assertEqual(response.context['alimentacao'], 23)
        self.assertEqual(response.context['medicacao'], 27)
        self.assertEqual(response.context['municao'], 32)  

        self.assertEqual(response.context['infectados_p'], 33.0)  
        self.assertEqual(response.context['n_infectados_p'], 67.0)  

        self.assertEqual(response.context['pontos_perdidos'], 190 )  















  
  


      
     


        




      


