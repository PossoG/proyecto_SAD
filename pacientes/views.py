

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Paciente, HistoriaClinica, Procedimiento
from .forms import ProcedimientoForm
from django.contrib import messages

@login_required
def mis_historias(request):
    """
    Lista todas las historias clínicas del paciente logueado.
    """
    perfil = get_object_or_404(Paciente, usuario=request.user)
    historias = HistoriaClinica.objects.filter(paciente=perfil).order_by('-fecha_registro')
    return render(request, 'pacientes/mis_historias.html', {'historias': historias})

@login_required
def detalle_historia(request, pk):
    """
    Muestra una historia clínica en particular, con sus procedimientos.
    """
    perfil = get_object_or_404(Paciente, usuario=request.user)
    historia = get_object_or_404(HistoriaClinica, pk=pk, paciente=perfil)
    procedimientos = historia.procedimientos.all()
    return render(request, 'pacientes/detalle_historia.html', {
        'historia': historia,
        'procedimientos': procedimientos
    })

@login_required
def agregar_procedimiento(request, historia_pk):
    """
    Añade un nuevo procedimiento o cirugía a la historia clínica dada.
    """
    perfil = get_object_or_404(Paciente, usuario=request.user)
    historia = get_object_or_404(HistoriaClinica, pk=historia_pk, paciente=perfil)

    if request.method == 'POST':
        form = ProcedimientoForm(request.POST)
        if form.is_valid():
            proc = form.save(commit=False)
            proc.historia = historia
            proc.save()
            messages.success(request, "Procedimiento agregado correctamente.")
            return redirect('pacientes:detalle_historia', pk=historia.pk)
    else:
        form = ProcedimientoForm()

    return render(request, 'pacientes/agregar_procedimiento.html', {
        'form': form,
        'historia': historia
    })
