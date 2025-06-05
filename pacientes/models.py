from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError
from django.utils import timezone
from citas.models import Cita  # importamos el modelo Cita de tu app “citas”

User = settings.AUTH_USER_MODEL  # 'usuarios.User'


class Paciente(models.Model):
    """
    Perfil de paciente: un perfil 1-a-1 para cada User cuyo role = 'paciente'.
    """
    usuario = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='perfil_paciente'
    )
    fecha_nacimiento = models.DateField(
        'Fecha de nacimiento',
        null=True,
        blank=True
    )
    telefono = models.CharField(
        'Teléfono',
        max_length=20,
        blank=True
    )
    direccion = models.CharField(
        'Dirección',
        max_length=200,
        blank=True
    )

    class Meta:
        verbose_name = 'Paciente'
        verbose_name_plural = 'Pacientes'

    def __str__(self):
        return f"{self.usuario.get_full_name()} ({self.usuario.email})"

    def clean(self):
        """
        Validamos que solo se cree un Paciente si el User asociado tiene role='paciente'.
        """
        if self.usuario.role != 'paciente':
            raise ValidationError("Solo se pueden crear perfiles de Paciente si el usuario tiene role='paciente'.")

    def save(self, *args, **kwargs):
        # Llamamos a clean() antes de guardar
        self.clean()
        super().save(*args, **kwargs)


class HistoriaClinica(models.Model):
    """
    Representa la ficha/historial de una visita. Puede vincularse a una Cita existente.
    """
    paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='historias'
    )
    cita = models.OneToOneField(
        Cita,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='historia_clinica'
    )
    fecha_registro = models.DateTimeField(
        'Fecha de registro',
        default=timezone.now
    )
    observaciones = models.TextField(
        'Observaciones generales',
        blank=True
    )

    class Meta:
        verbose_name = 'Historia Clínica'
        verbose_name_plural = 'Historias Clínicas'
        ordering = ['-fecha_registro']

    def __str__(self):
        return f"Historia #{self.id} – {self.paciente.usuario.get_full_name()} ({self.fecha_registro.date()})"


class Procedimiento(models.Model):
    """
    Almacena cada procedimiento o cirugía realizada en una visita (HistoriaClinica).
    """
    HISTORIA_CHOICES = (
        ('procedimiento', 'Procedimiento'),
        ('cirugia', 'Cirugía'),
    )

    historia = models.ForeignKey(
        HistoriaClinica,
        on_delete=models.CASCADE,
        related_name='procedimientos'
    )
    categoria = models.CharField(
        'Tipo de registro',
        max_length=15,
        choices=HISTORIA_CHOICES,
        default='procedimiento'
    )
    descripcion = models.TextField(
        'Descripción detallada',
        blank=True,
    )
    fecha = models.DateField(
        'Fecha del procedimiento o cirugía',
        default=timezone.now
    )
    hora_inicio = models.TimeField(
        'Hora inicio',
        null=True,
        blank=True
    )
    hora_fin = models.TimeField(
        'Hora fin',
        null=True,
        blank=True
    )
    dentista = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='procedimientos_realizados'
    )
    observaciones = models.TextField(
        'Observaciones posteriores',
        blank=True
    )

    class Meta:
        verbose_name = 'Procedimiento/Cirugía'
        verbose_name_plural = 'Procedimientos y Cirugías'
        ordering = ['-fecha']

    def __str__(self):
        return f"{self.get_categoria_display()} – {self.historia.paciente.usuario.get_full_name()} ({self.fecha})"


# Señal para crear Perfil de Paciente automáticamente cuando se crea un User con role='paciente'
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def crear_perfil_paciente(sender, instance, created, **kwargs):
    """
    Cada vez que un User se crea con role='paciente', generamos automáticamente su perfil Paciente.
    """
    if created and instance.role == 'paciente':
        Paciente.objects.create(usuario=instance)

