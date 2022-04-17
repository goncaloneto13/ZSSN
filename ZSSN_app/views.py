from multiprocessing import context
from django.shortcuts import render,redirect
from ZSSN_app.forms import AcusacoesForm, InventarioForm, SobreviventeForm,LocalForm
from ZSSN_app.models import Inventario, Sobrevivente

# Create your views here.

def home(request):
    sobreviventes = Sobrevivente.objects.all()
    context = {
        'sobreviventes': sobreviventes
    }
    return render(request,'ZSSN/home.html',context)

def add_sobreviventes(request):
    form = SobreviventeForm(request.POST or None)   
    form_inventario = InventarioForm(request.POST or None)

    if request.POST:
        if form.is_valid() and form_inventario.is_valid():
            inventario = form_inventario.save()
            sobrevivente = form.save(commit=False)
            sobrevivente.inventario = inventario
            sobrevivente.save()
            
            return redirect('home')

    context = { 
        'form':form,
        'form_inventario': form_inventario
    }
    return render(request, 'ZSSN/add_sobreviventes.html', context)

def edit_sobrevivente(request, sobrevivente_pk):
    sobrevivente = Sobrevivente.objects.get(pk=sobrevivente_pk)
    outros_sob = Sobrevivente.objects.all()
    form = LocalForm(request.POST or None, instance=sobrevivente)   

    idade = sobrevivente.idade()
    sexo = sobrevivente.Sexo()

    outros_id = []
    for o in outros_sob:
        outros_id.append(o.id)
   
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('edit_sobrevivente',sobrevivente_pk)

    context = {
        'form': form,
        'sobrevivente': sobrevivente,
        'outros_sob': outros_sob,
        'outros_id': outros_id,
        'idade': idade,
        'sexo': sexo
    }        
    return render(request, 'ZSSN/edit_sobrevivente.html', context)

def trocar_itens(request,sobrevivente_pk,outro_pk):
    sobrevivente = Sobrevivente.objects.get(pk=sobrevivente_pk)
    outro_s = Sobrevivente.objects.get(pk=outro_pk)

    #inventario0 = Inventario.objects.get(sobrevivente_id=sobrevivente_pk)
    #inventario1= Inventario.objects.get(sobrevivente_id=outro_pk)
   
    form_s0 = InventarioForm(request.POST or None, instance=sobrevivente.inventario)
    form_s1 = InventarioForm(request.POST or None, instance=outro_s.inventario)

    itens0 = sobrevivente.inventario.quant_itens()
    itens1 = outro_s.inventario.quant_itens()

    if request.POST:
        if form_s0.is_valid() and form_s1.is_valid():
            s0_novos_itens= request.POST.get('s0_novos_itens',None).split(',')
            s0_itens = request.POST.get('s0_itens',None).split(',')
            s1_novos_itens = request.POST.get('s1_novos_itens',None).split(',')
            s1_itens = request.POST.get('s1_itens',None).split(',')

            print( s0_novos_itens, s0_itens, s1_novos_itens, s1_itens)
            novos_itens0 = []
            novos_itens1 = []

            for i in range(0,4):
                novos_itens0.append(int(s0_itens[i]) + int(s1_novos_itens[i]))
                novos_itens1.append(int(s1_itens[i]) + int(s0_novos_itens[i]))
            print( novos_itens0, novos_itens1)    

            form_s0_ = form_s0.save(commit=False)
            form_s0_.agua = novos_itens0[0]
            form_s0_.alimentacao = novos_itens0[1]
            form_s0_.medicacao = novos_itens0[2]
            form_s0_.municao = novos_itens0[3]
            form_s0_.save()
  
            form_s1_ = form_s1.save(commit=False)
            form_s1_.agua = novos_itens1[0]
            form_s1_.alimentacao = novos_itens1[1]
            form_s1_.medicacao = novos_itens1[2]
            form_s1_.municao = novos_itens1[3]
            form_s1_.save()
     
            
            return redirect('trocar_itens',sobrevivente_pk,outro_pk)
  
    context ={
        'outro_s':outro_s,
        'sobrevivente':sobrevivente,
        'qtd_itens0':itens0,
        'qtd_itens1':itens1,
        'form_s0':form_s0,
        'form_s1':form_s1,
       
    }
    return render(request, 'ZSSN/trocar_itens.html', context)

def acusar(request, sobrevivente_pk, acusado_pk):
    acusado = Sobrevivente.objects.get(pk=acusado_pk)
    acusar_form = AcusacoesForm(request.POST or None, instance=acusado)
    sobrevivente = Sobrevivente.objects.get(pk=sobrevivente_pk)
    form = LocalForm(request.POST or None, instance=sobrevivente)
   
  
    if request.POST:   
    
        if acusar_form.is_valid():
            print(acusado.acusacoes)
            acusar_form_ = acusar_form.save(commit=False)
            acusar_form_.acusacoes += 1

          
            form_ = form.save(commit=False)
            form_.infectados_relatados.append(acusado_pk)
            form_.save()
            

            if (acusado.acusacoes >= 3):     
                acusar_form_.infectado = True

            acusar_form_.save()
            acusar_form.save()    
            return redirect('edit_sobrevivente',sobrevivente_pk)

             
   
    outros_sob = Sobrevivente.objects.all()
   
    outros_id = []
    for o in outros_sob:
        outros_id.append(o.id)
   

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'sobrevivente': sobrevivente,
        'outros_sob': outros_sob,
        'outros_id': outros_id,
        'acusar_form': acusar_form,
        'acusado': acusado
    }        
    return render(request, 'ZSSN/acusar_infectado.html', context)  


def relatorio(request):

    sobreviventes = Sobrevivente.objects.all()
    inventarios = Inventario.objects.all()
    q_inventarios = len(inventarios)
    infectados = 0
    agua = 0
    alimentacao = 0
    medicacao =0
    municao =0
    pontos_perdidos = 0

    for sobrevivente in sobreviventes:
        if sobrevivente.infectado == True:
            infectados += 1
            itens = sobrevivente.inventario
            pontos_perdidos += itens.total_pontos()

        itens = sobrevivente.itens

    for item in inventarios:
        agua += item.agua
        alimentacao += item.alimentacao
        medicacao += item.medicacao
        municao += item.municao

    agua = int(agua/q_inventarios)
    alimentacao = int(alimentacao/q_inventarios)
    medicacao = int(medicacao/q_inventarios)
    municao = int(municao/q_inventarios)

    q_item =  [agua, alimentacao,medicacao,municao]

    itens = zip(itens, q_item)

    infectados_p = round(infectados/len(sobreviventes),2) * 100   
    n_infectados_p = round((len(sobreviventes) - infectados)/len(sobreviventes),2) * 100

    context = {
        'infectados_p':infectados_p,
        'n_infectados_p':n_infectados_p,
        'agua':agua,
        'alimentacao': alimentacao,
        'medicacao': medicacao,
        'municao': municao,
        'pontos_perdidos': pontos_perdidos,
        'itens': itens
    }
    return render(request, 'ZSSN/relatorio.html',context)


    

