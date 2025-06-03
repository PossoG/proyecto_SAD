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
