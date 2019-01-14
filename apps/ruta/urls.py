from django.urls import path

from apps.ruta import views

app_name = 'ruta'

urlpatterns = [
    path('nuevo', views.rutaNuevoVista, name='nuevoVista'),
    path('listar', views.rutaListarVista, name='listarVista')
]