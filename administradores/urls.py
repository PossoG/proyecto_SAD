# doctores/urls.py

from django.urls import path
from . import views

app_name = 'administradores'

urlpatterns = [
    # Al acceder a /doctores/ (prefijo definido en SAD/urls.py), Django llamará a views.index
    path('', views.index, name='index'),
    path('inventario-registrar/', views.inventario_registrar, name='inventario-registrar'),
    path('inventario-alertas/', views.inventario_alertas, name='inventario-alertas'),
    path('proveedores-registrar/', views.proveedores_registrar, name='proveedores-registrar'),

]