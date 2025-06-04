# citas/forms.py
from django import forms
from .models import Cita
from django.utils import timezone
from datetime import date

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['tipo', 'fecha', 'hora']
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date', 'min': date.today().isoformat()}),
            'hora': forms.TimeInput(attrs={'type': 'time'}),
        }

    def __init__(self, *args, **kwargs):
        self.paciente = kwargs.pop('paciente', None)
        super().__init__(*args, **kwargs)

    def clean_fecha(self):
        fecha = self.cleaned_data.get('fecha')
        if fecha < date.today():
            raise forms.ValidationError("No puedes agendar una cita en una fecha pasada.")
        return fecha

    def clean(self):
        cleaned = super().clean()
        fecha = cleaned.get('fecha')
        hora = cleaned.get('hora')
        if fecha and hora:
            # Verificar que no exista otra cita el mismo día y hora
            qs = Cita.objects.filter(fecha=fecha, hora=hora, estado__in=['pendiente', 'confirmada'])
            if self.instance.pk:
                # Estamos reprogramando: excluir la cita actual
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise forms.ValidationError("Ya hay una cita programada en esa fecha y hora. Por favor elige otra.")
        return cleaned

    def save(self, commit=True):
        cita = super().save(commit=False)
        # Asignar el paciente que pasó la vista
        if self.paciente:
            cita.paciente = self.paciente
        if commit:
            cita.save()
        return cita
    

