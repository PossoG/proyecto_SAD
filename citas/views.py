from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Cita
from .forms import CitaForm
from django.contrib import messages

@login_required
def mis_citas(request):
    """
    Lista todas las citas del paciente autenticado, ordenadas por fecha.
    """
    citas = Cita.objects.filter(paciente=request.user).order_by('fecha', 'hora')
    return render(request, 'citas/mis_citas.html', {'citas': citas})

@login_required
def crear_cita(request):
    """
    Permite al paciente crear una nueva cita. 
    Asigna dentista automáticamente en el save() del modelo.
    """
    if request.method == 'POST':
        form = CitaForm(request.POST, paciente=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Cita agendada correctamente.")
            return redirect('citas:mis_citas')
    else:
        form = CitaForm(paciente=request.user)
    return render(request, 'citas/crear_cita.html', {'form': form})

@login_required
def reprogramar_cita(request, pk):
    """
    Permite al paciente editar (reprogramar) una cita existente siempre que esté en estado 'pendiente' o 'confirmada'.
    """
    cita = get_object_or_404(Cita, pk=pk, paciente=request.user)
    if cita.estado not in ['pendiente', 'confirmada']:
        messages.error(request, "Solo puedes reprogramar citas pendientes o confirmadas.")
        return redirect('citas:mis_citas')

    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita, paciente=request.user)
        if form.is_valid():
            cita.estado = 'reprogramada'
            form.save()
            messages.success(request, "Cita reprogramada correctamente.")
            return redirect('citas:mis_citas')
    else:
        form = CitaForm(instance=cita, paciente=request.user)
    return render(request, 'citas/reprogramar_cita.html', {'form': form, 'cita': cita})

@login_required
def cancelar_cita(request, pk):
    """
    Cancela la cita (marca estado como 'cancelada'). 
    Podrías decidir borrar el registro o simplemente cambiar el estado.
    Aquí lo marcamos como 'cancelada'.
    """
    cita = get_object_or_404(Cita, pk=pk, paciente=request.user)
    if request.method == 'POST':
        cita.estado = 'cancelada'
        cita.save()
        messages.success(request, "Cita cancelada correctamente.")
        return redirect('citas:mis_citas')
    return render(request, 'citas/cancelar_cita.html', {'cita': cita})


from datetime import time, timedelta, datetime, date

def obtener_horas_disponibles(fecha):
    """
    Genera un listado de objetos datetime.time para cada slot libre en un día dado.
    """
    hora_inicio = time(hour=8, minute=0)
    hora_fin = time(hour=17, minute=0)
    intervalo = timedelta(minutes=30)

    slots = []
    actual = datetime.combine(fecha, hora_inicio)
    fin = datetime.combine(fecha, hora_fin)

    while actual <= fin:
        slots.append(actual.time())
        actual += intervalo
    return slots

@login_required
def crear_cita(request):
    fecha_elegida = None
    horas_ocupadas = []
    horas_libres = []

    if request.method == 'POST':
        form = CitaForm(request.POST, paciente=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, "Cita agendada correctamente.")
            return redirect('citas:mis_citas')
    else:
        form = CitaForm(paciente=request.user)

    # Si el usuario ya seleccionó una fecha (por ejemplo, via GET ?fecha=2025-06-10)
    if request.GET.get('fecha'):
        try:
            fecha_elegida = date.fromisoformat(request.GET.get('fecha'))
            # Obtener horas ocupadas de ese día
            citas_dia = Cita.objects.filter(fecha=fecha_elegida, estado__in=['pendiente', 'confirmada'])
            horas_ocupadas = [cita.hora for cita in citas_dia]
            # Calcular slots y filtrar los ocupados
            posibles_horas = obtener_horas_disponibles(fecha_elegida)
            horas_libres = [h for h in posibles_horas if h not in horas_ocupadas]
        except ValueError:
            fecha_elegida = None

    return render(request, 'citas/crear_cita.html', {
        'form': form,
        'fecha_elegida': fecha_elegida,
        'horas_libres': horas_libres,
    })


