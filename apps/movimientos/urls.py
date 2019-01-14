from django.urls import path

from apps.movimientos import views

app_name = 'movimientos'

urlpatterns = [
    # PRESTAMOS
    path('prestamo/nuevo/', views.prestamoNuevoVista, name='prestamoNuevoVista'),
    path('prestamo/listar/', views.prestamoListarVista, name='prestamoListarVista')
]