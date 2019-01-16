from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.db.models import Q
from django.shortcuts import render, redirect
from django.http import JsonResponse

from apps.cliente.models import Cliente
from apps.movimientos.models import Prestamo

from datetime import datetime, date

import json

# Create your views here.

# VISTAS CLIENTE
@login_required
def clienteNuevoVista(request):
    return render(request, 'cliente/cliente-nuevo.html')

@login_required
def clienteListarVista(request):
    return render(request, 'cliente/cliente-listar.html')

# SERVICIOS CLIENTE
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
        res = {}
        res['cliente'] = prestamo['cliente']
        res['dni'] = cliente.dni
        res['direccion'] = cliente.direccion
        res['fechaIngreso'] = str(cliente.fechaIngreso)
        resultado.append(res)
    
    return JsonResponse(resultado, safe=False)

def clienteBuscarDNI(request, dni):
    clientes = Cliente.objects.filter(activo=True, dni__contains=dni)
    data = serializers.serialize('json', clientes, fields=('nombres', 'apPaterno', 'apMaterno', 'dni'))    
    print(json.loads(data))

    return JsonResponse(data, safe=False)

def clienteBuscarNombre(request, nombres):
    busqueda = nombres.strip().split()
    clientes = nombresMatching(busqueda)
    data = serializers.serialize('json', clientes, fields=('nombres', 'apPaterno', 'apMaterno', 'dni'))
    print(data)

    return JsonResponse(data, safe=False)



# FUNCIONES AUXILIARES
"""
Busca los clientes registrados y los amarra a sus respectivos prestamos
de no tener prestamo, se le asigna False indicando que no tiene prestamos
retorna un array de jsons con todos los clientes y sus respectivos prestamos
"""
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

"""
obtiene los valores de busqueda en un array de strings, luego concatena las
condicionales para tener una query completa y obtener los clientes mediante
nombre || apPaterno ||apMaterno
retorna un query de clientes
"""

def nombresMatching(nombres):
    longitud = len(nombres)
    q = Q()
    if longitud == 1:
        q |= Q(nombres__icontains=nombres[0])
        q |= Q(apPaterno__icontains=nombres[0])
        q |= Q(apMaterno__icontains=nombres[0])
    elif longitud == 2:
        q |= Q(nombres__icontains=nombres[0])
        q |= Q(nombres__icontains=nombres[1])
        q &= Q(apPaterno__icontains=nombres[1])
    else:
        q |= Q(nombres__icontains = nombres[0])
        q |= Q(nombres__icontains = nombres[1])
        q |= Q(apPaterno__icontains = nombres[2])
        q |= Q(apMaterno__icontains = nombres[3])
    
    
    return Cliente.objects.filter(q)