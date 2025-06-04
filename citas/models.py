from django.db import models
from django.conf import settings
from django.utils import timezone
import random

User = settings.AUTH_USER_MODEL  # 'usuarios.User'

class TipoCita(models.TextChoices):
    NORMAL = 'normal', 'Normal'
    PROCEDIMIENTO = 'procedimiento', 'Procedimiento'
    CIRUGIA = 'cirugia', 'Cirugía'

class Cita(models.Model):
    paciente = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='citas_paciente'
    )
    dentista = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='citas_dentista'
    )
    tipo = models.CharField(
        max_length=15,
        choices=TipoCita.choices,
        default=TipoCita.NORMAL
    )
    fecha = models.DateField()
    hora = models.TimeField()
    estado = models.CharField(
        max_length=20,
        choices=(
            ('pendiente', 'Pendiente'),
            ('confirmada', 'Confirmada'),
            ('reprogramada', 'Reprogramada'),
            ('cancelada', 'Cancelada'),
        ),
        default='pendiente'
    )
    # (opcional) campo que guarde cuándo se creó la cita
    creado_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Cita #{self.id} - {self.paciente} con {self.dentista} el {self.fecha} a las {self.hora}"
    
    def asignar_dentista_aleatorio(self):
        """
        Elige un dentista/cirujano aleatorio disponible (con role='dentista' o 'cirujano').
        Se asume que el administrador marcó con el flag `is_active` quienes están disponibles.
        """
        from django.contrib.auth import get_user_model
        Usuario = get_user_model()
        # Filtrar dentistas y cirujanos activos
        candidatos = Usuario.objects.filter(role__in=['dentista', 'cirujano'], is_active=True)
        if not candidatos.exists():
            return None
        return random.choice(candidatos)

    def save(self, *args, **kwargs):
        """
        Al guardar una cita nueva, si no se ha asignado dentista manualmente,
        se asigna uno aleatorio.
        """
        is_nueva = self.pk is None
        if is_nueva and not self.dentista:
            self.dentista = self.asignar_dentista_aleatorio()
        super().save(*args, **kwargs)

