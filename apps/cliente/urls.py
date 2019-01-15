from django.urls import path

from apps.cliente import views

app_name = 'cliente'

urlpatterns = [
    # VISTAS
    path('nuevo/', views.clienteNuevoVista, name='nuevoVista'),
    path('listar/', views.clienteListarVista, name='listarVista'),
    
    # SERVICIOS
    path('api-nuevo/', views.clienteNuevoServicio, name='nuevoServicio'),
    path('api-listar/', views.clienteListarServicio, name='listarServicio')
]