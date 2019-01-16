from django.urls import path

from apps.movimientos import views

app_name = 'movimientos'

urlpatterns = [
    # PRESTAMOS
    # PRESTAMOS VISTAS
    path('prestamo/nuevo/', views.prestamoNuevoVista, name='prestamoNuevoVista'),
    path('prestamo/listar/', views.prestamoListarVista, name='prestamoListarVista'),

    #PRESTAMOS SERVICIOS
    path('prestamo/api-nuevo/', views.prestamoNuevoServicio, name='prestamoNuevoServicio'),
    path('prestamo/api-listar/', views.prestamoListarServicio, name='prestamoListarServicio')
]