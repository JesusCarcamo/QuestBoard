from django.shortcuts import render
from django.conf import settings

# Create your views here.
def inicio(request):
    context = {
    }
    return render(request, "inicio.html",context)

def ingresar(request):
    context = {
    }
    return render(request, "ingresar.html",context)

def perfil(request):
    context = {
    }
    return render(request, "perfil.html",context)


