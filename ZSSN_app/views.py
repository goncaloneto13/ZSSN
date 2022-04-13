from django.shortcuts import render,redirect
from ZSSN_app.forms import SobreviventeForm
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
 
