from django.urls import path

from apps.cliente import views

app_name = 'cliente'

urlpatterns = [
    path('nuevo/', views.clienteNuevoVista, name='nuevoVista'),
    path('listar/', views.clienteListarVista, name='listarVista'),
    
]