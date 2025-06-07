from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'doctores/resultados_doctor.html')

def historial_clinico_doctor(request):
    return render(request, 'doctores/historial_clinico_doctor.html')

def historial_clinico_doctor_agregar(request):
    return render(request, 'doctores/Crear.html')


