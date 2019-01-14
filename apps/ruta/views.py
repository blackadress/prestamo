from django.shortcuts import render

# Create your views here.
def rutaNuevoVista(request):
    return render(request, 'ruta/ruta-nuevo.html')

def rutaListarVista(request):
    return render(request, 'ruta/ruta-listar.html')