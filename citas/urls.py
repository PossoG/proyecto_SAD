from django.urls import path
from . import views

app_name = 'citas'
urlpatterns = [
    path('', views.mis_citas, name='mis_citas'),
    path('crear/', views.crear_cita, name='crear_cita'),
    path('reprogramar/<int:pk>/', views.reprogramar_cita, name='reprogramar_cita'),
    path('cancelar/<int:pk>/', views.cancelar_cita, name='cancelar_cita'),
]
