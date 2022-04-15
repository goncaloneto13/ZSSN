from multiprocessing import context
from django.shortcuts import render,redirect
from ZSSN_app.forms import AcusacoesForm, ItensForm, SobreviventeForm,LocalForm
from ZSSN_app.models import Sobrevivente

# Create your views here.

def home(request):
    sobreviventes = Sobrevivente.objects.all()
    context = {
        'sobreviventes': sobreviventes
    }
    return render(request,'ZSSN/home.html',context)

def add_sobreviventes(request):
    form = SobreviventeForm(request.POST or None)   
    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')

    context = { 
        'form':form
    }
    return render(request, 'ZSSN/add_sobreviventes.html', context)

def edit_sobrevivente(request, sobrevivente_pk):
    sobrevivente = Sobrevivente.objects.get(pk=sobrevivente_pk)
    outros_sob = Sobrevivente.objects.all()
    form = LocalForm(request.POST or None, instance=sobrevivente)   

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
        'outros_id': outros_id
    }        
    return render(request, 'ZSSN/edit_sobrevivente.html', context)

def trocar_itens(request, outro_pk,sobrevivente_pk):
    sobrevivente = Sobrevivente.objects.get(pk=sobrevivente_pk)
    outro_s = Sobrevivente.objects.get(pk=outro_pk)
    form_s = ItensForm(request.POST or None, instance=sobrevivente)
    form_so = ItensForm(request.POST or None, instance=outro_s)

    itens1 = [sobrevivente.Água,sobrevivente.Alimento,sobrevivente.Medicação,sobrevivente.Munição]
    itens2 = [outro_s.Água,outro_s.Alimento,outro_s.Medicação,outro_s.Munição]
    Itens = zip(sobrevivente.Itens,itens1)

    if request.POST:
        print('okok')
        if form_s.is_valid() and form_so.is_valid():
            s1_novos_itens= request.POST.get('s1_novos_itens',None)
            s1_itens = request.POST.get('s1_itens',None)
            s2_novos_itens = request.POST.get('s2_novos_itens',None)
            s2_itens = request.POST.get('s2_itens',None)

            print( s1_novos_itens, s1_itens, s2_novos_itens, s2_itens)
            novos_itens1 = []
            novos_itens2 = []
            for i in range(0,8,2):
                novos_itens1.append(int(s1_itens[i]) + int(s2_novos_itens[i]))
                novos_itens2.append(int(s2_itens[i]) + int(s1_novos_itens[i]))

            form_s_ = form_s.save(commit='false')
            form_s_.Água = novos_itens1[0]
            form_s_.Alimento = novos_itens1[1]
            form_s_.Medicamento = novos_itens1[2]
            form_s_.Munição = novos_itens1[3]
            form_s_.save()

            form_so_ = form_so.save(commit='false')
            form_so_.Água = novos_itens2[0]
            form_so_.Alimento = novos_itens2[1]
            form_so_.Medicamento = novos_itens2[2]
            form_so_.Munição = novos_itens2[3]
            form_so_.save()
            print( novos_itens1, novos_itens2)
            return redirect('trocar_itens',outro_pk,sobrevivente_pk)
  
    context ={
        'outro_s':outro_s,
        'sobrevivente':sobrevivente,
        'itens1': Itens,
        'qtd_itens1':itens1,
        'qtd_itens2':itens2,
        'form_s':form_s,
        'form_so':form_so

    }
    return render(request, 'ZSSN/trocar_itens.html', context)

def acusar(request, sobrevivente_pk, acusado_pk):
    acusado = Sobrevivente.objects.get(pk=acusado_pk)
    acusar_form = AcusacoesForm(request.POST or None, instance=acusado)
  
    if request.POST:   
    
        if acusar_form.is_valid():
            print(acusado.acusacoes)
            acusar_form_ = acusar_form.save(commit=False)
            acusar_form_.acusacoes += 1
            if (acusado.acusacoes >= 3):     
                acusar_form_.Infectado = True

            acusar_form_.save()
            acusar_form.save()    
            return redirect('edit_sobrevivente',sobrevivente_pk)

             
    sobrevivente = Sobrevivente.objects.get(pk=sobrevivente_pk)
    outros_sob = Sobrevivente.objects.all()
    form = LocalForm(request.POST or None, instance=sobrevivente)

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

