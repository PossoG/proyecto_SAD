from django import forms
from .models import Procedimiento

class ProcedimientoForm(forms.ModelForm):
    class Meta:
        model = Procedimiento
        fields = [
            'categoria',
            'descripcion',
            'fecha',
            'hora_inicio',
            'hora_fin',
            'dentista',
            'observaciones',
        ]
        widgets = {
            'fecha': forms.DateInput(attrs={'type': 'date'}),
            'hora_inicio': forms.TimeInput(attrs={'type': 'time'}),
            'hora_fin': forms.TimeInput(attrs={'type': 'time'}),
        }
