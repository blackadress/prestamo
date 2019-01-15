from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse

from apps.cliente.models import Cliente
from apps.movimientos.models import Prestamo

import json

# Create your views here.

@login_required
def clienteNuevoVista(request):
    return render(request, 'cliente/cliente-nuevo.html')

@login_required
def clienteListarVista(request):
    return render(request, 'cliente/cliente-listar.html')

@login_required
def clienteNuevoServicio(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(body)

    cliente = Cliente(
        nombres=body['nombres'],
        apPaterno=body['apPat'],
        apMaterno=body['apMat'],
        dni=body['dni'],
        direccion=body['direccion'],
        activo=True,
        latitud=body['latitud'],
        longitud=body['longitud']
    )

    cliente.save()

    return JsonResponse({'exito':True})

@login_required
def clienteListarServicio(request):
    resultado = []
    clientes = Cliente.objects.all()

    clientesPrestamo = buscarPrestamoCliente(clientes)

    for cliente, prestamo in zip(clientes, clientesPrestamo):
        json = {}
        json['cliente'] = prestamo['cliente']
        json['dni'] = cliente.dni
        json['direccion'] = cliente.direccion
        json['fechaIngreso'] = cliente.fechaIngreso
        resultado.append(json)
    
    return JsonResponse(resultado, safe=False)

# FUNCIONES AUXILIARES
def buscarPrestamoCliente(clientes):
    prestamos = []
    for cliente in clientes:
        json = {}
        prestamo = Prestamo.objects.filter(cliente=cliente, aprobado=True, activo=True)
        if prestamo:
            json['cliente'] = cliente.nombreCompleto
            for pres in prestamo:
                json['prestamoId'] = pres.id
        else:
            json['cliente'] = cliente.nombreCompleto
            json['prestamoId'] = False
        
        prestamos.append(json)

    return prestamos