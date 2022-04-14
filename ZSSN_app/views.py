from django.shortcuts import render,redirect
from ZSSN_app.forms import SobreviventeForm,LocalForm
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

    if request.POST:
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {
        'form': form,
        'sobrevivente': sobrevivente,
        'outros_sob': outros_sob
    }        
    return render(request, 'ZSSN/edit_sobrevivente.html', context)
