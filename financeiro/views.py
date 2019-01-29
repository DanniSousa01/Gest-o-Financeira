from django.shortcuts import render
from . models import Usuario
# Create your views here.

def home(request):
    return render (request, 'home.html', {})

def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render (request, 'usuarios/list.html', {'usuarios': usuarios})

def usuario_show(request, usuario_id):
    usuario = Usuario.objects.get(pk=cliente_id)
    return render(request, 'usuarios/show.html', {'usuario': usuario})