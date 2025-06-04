# bienvenido/urls.py
from django.urls import path
from . import views

app_name = 'bienvenido'

urlpatterns = [
    path('', views.home, name='home'),
    path('citas/', views.citas_medicas, name='citas'),
    path('resultados/', views.ver_resultados, name='resultados'),
    path('crear-cuenta/', views.crear_cuenta, name='crear-cuenta'),
    path('agendar/', views.agendar_cita, name='agendar-cita'),
    path('consultar-cita/', views.consultar_cita, name='consultar-cita'),
    path('cancelar-cita/', views.cancelar_cita, name='cancelar-cita'),
    path('reprogramar-cita1/', views.reprogramar_cita1, name='reprogramar-cita1'),
    path('reprogramar-cita2/', views.reprogramar_cita2, name='reprogramar-cita2'),
    path('historial-clinico/', views.historial_clinico, name='historial-clinico'),
    path('notificacion/', views.notificacion, name='notificacion'),
    path('perfil-usuario/', views.perfil_usuario, name='perfil-usuario'),
    path('perfil-usuario-editar/', views.perfil_usuario_editar, name='perfil-usuario-editar'),
    path('gestionar-familiares/', views.gestionar_familiares, name='gestionar-familiares'),
    path('inicio-sesion/', views.inicio_sesion, name='inicio-sesion'),
    path('recuperacion-cuenta/', views.recuperacion_cuenta, name='recuperacion-cuenta'),
    
]
