# doctores/urls.py

from django.urls import path
from . import views

app_name = 'doctores'

urlpatterns = [
    # Al acceder a /doctores/ (prefijo definido en SAD/urls.py), Django llamará a views.index
    path('', views.index, name='index'),
    path('historial_clinico_doctor/', views.historial_clinico_doctor, name='historial_clinico_doctor'),
    
    
    
    
    # Si más adelante quieres agregar rutas adicionales para “doctores”, por ejemplo:
    # path('perfil/<int:id>/', views.perfil_doctor, name='perfil'),
    # path('lista/', views.lista_doctores, name='lista'),
]