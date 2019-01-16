from django.contrib.auth.decorators import login_required
from djang.core import serializers
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import JsonResponse

from apps.movimientos.models import Prestamo
from apps.empleado.models import Empleado
from apps.caja.models import Caja

import json

# Create your views here.

# PRESTAMO VISTAS
@login_required
def prestamoNuevoVista(request):
    cajas = Caja.objects.all()
    supervisores = Empleado.objects.filter(rol='supervisor', activo=True)

    context = {
        'cajas': cajas,
        'supervisores': supervisores
    }

    return render(request, 'movimientos/prestamo/prestamo-nuevo.html', context)

@login_required
def prestamoListarVista(request):
    return render(request, 'movimientos/prestamo/prestamo-listar.html')

# PRESTAMO SERVICIOS
@login_required
def prestamoNuevoServicio(request):
    usuario = request.user
    # cajero = Empleado.objects.get(usuario=usuario)

    # print(request.user)

    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    print(body)

    # prestamo = Prestamo(
    #     monto=body['monto'],
    #     supervisor_id=body['supervisorId'],
    #     cajero=cajero,
    #     caja_id=body['cajaId'],
    #     cliente_id=body['clienteId']
    # )

    # prestamo.save()

    return JsonResponse({'exito': True})

@login_required
def prestamoListarServicio(request):
    prestamos = Prestamo.objects.all()
    data = serializers.serialize('json', prestamos, fields=('fechaCreacion', 'monto', 'supervisor', 'caja', 'cliente'))

    return JsonResponse(data, safe=False)
