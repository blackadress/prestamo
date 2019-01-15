from django.shortcuts import render
from django.http import JsonResponse

import ast

# Create your views here.

def clienteNuevoVista(request):
    return render(request, 'cliente/cliente-nuevo.html')

def clienteListarVista(request):
    return render(request, 'cliente/cliente-listar.html')

def clienteNuevoServicio(request):
    print('req post', request.POST)
    print('data', request.POST['data'])
    data = request.POST['data']
    data = ast.literal_eval(data)

    for key, value in data.items():
        print(value)

    return JsonResponse(data, safe=False)