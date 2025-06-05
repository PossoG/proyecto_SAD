from django.contrib import admin

from .models import Paciente, HistoriaClinica, Procedimiento

@admin.register(Paciente)
class PacienteAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha_nacimiento', 'telefono')
    search_fields = ('usuario__email', 'usuario__first_name', 'usuario__last_name')
    list_filter = ('usuario__role',)

@admin.register(HistoriaClinica)
class HistoriaClinicaAdmin(admin.ModelAdmin):
    list_display = ('paciente', 'cita', 'fecha_registro')
    search_fields = ('paciente__usuario__email',)
    list_filter = ('fecha_registro',)

@admin.register(Procedimiento)
class ProcedimientoAdmin(admin.ModelAdmin):
    list_display = ('historia', 'categoria', 'fecha', 'dentista')
    search_fields = ('historia__paciente__usuario__email',)
    list_filter = ('categoria', 'fecha')

