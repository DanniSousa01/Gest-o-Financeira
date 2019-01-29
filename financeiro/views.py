from django.shortcuts import render
from . models import Usuario, Despesas
# Create your views here.

def home(request):
    return render (request, 'home.html', {})

def usuario_list(request):
    usuarios = Usuario.objects.all()
    return render (request, 'usuarios/list.html', {'usuarios': usuarios})

def usuario_show(request, usuario_id):
    usuario = Usuario.objects.get(pk=usuario_id)
    return render(request, 'usuarios/show.html', {'usuario': usuario})

def despesa_list (request):
    despesas = Despesas.objects.all()
    return render(request, 'despesas/list.html', {'despesas': despesas}) 

def despesa_show(request, despesa_id):
    despesa = Despesas.objects.get(pk=despesa_id)
    return render(request, 'despesas/show.html', {'despesa': despesa})