from django.shortcuts import render

# Create your views here.

def prestamoNuevoVista(request):
    return render(request, 'movimientos/prestamo/prestamo-nuevo.html')

def prestamoListarVista(request):
    return render(request, 'movimientos/prestamo/prestamo-listar.html')