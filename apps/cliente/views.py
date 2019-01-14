from django.shortcuts import render

# Create your views here.

def clienteNuevoVista(request):
    return render(request, 'cliente/cliente-nuevo.html')

def clienteListarVista(request):
    return render(request, 'cliente/cliente-listar.html')