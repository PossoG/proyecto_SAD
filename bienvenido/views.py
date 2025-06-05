from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'bienvenido/index.html')

def citas_medicas(request):
    return render(request, 'bienvenido/citas.html')

def ver_resultados(request):
    return render(request, 'bienvenido/resultados.html')

def primera_vista(request):
    return render(request, 'bienvenido/primera_vista.html')

def crear_cuenta(request):
    return render(request, 'bienvenido/crear_cuenta.html')

def agendar_cita(request):
    return render(request, 'bienvenido/Agendar.html')

def consultar_cita(request):
    return render(request, 'bienvenido/consultar-citas.html')

def cancelar_cita(request):
    return render(request, 'bienvenido/Cancelar.html')

def reprogramar_cita1(request):
    return render(request, 'bienvenido/reprogramar_uno.html')

def reprogramar_cita2(request):
    return render(request, 'bienvenido/reprogramar2.html')

def historial_clinico(request):
    return render(request, 'bienvenido/historial_clinico.html')

def notificacion(request):
    return render(request, 'bienvenido/Notificaciones.html')

def perfil_usuario(request):
    return render(request, 'bienvenido/perfil_usuario.html')

def perfil_usuario_editar(request):
    return render(request, 'bienvenido/perfil_usuario_editar.html')

def gestionar_familiares(request):
    return render(request, 'bienvenido/gestionar_familiares.html')

def inicio_sesion(request):
    return render(request, 'bienvenido/InicioSesion.html')

def recuperacion_cuenta(request):
    return render(request, 'bienvenido/Recuperacion.html')