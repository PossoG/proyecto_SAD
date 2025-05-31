# usuarios/models.py

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    """
    Manager personalizado para crear usuarios y superusuarios usando correo.
    """
    def create_user(self, email, first_name, last_name, role, password=None, **extra_fields):
        """
        Crea y guarda un usuario regular.
        Normaliza role a minúsculas antes de crear.
        """
        if not email:
            raise ValueError("El usuario debe tener un correo electrónico.")
        email = self.normalize_email(email)

        # Asegurarnos de que role se guarde siempre en minúscula
        role_normalizado = role.lower()
        if role_normalizado not in dict(User.ROLES).keys():
            raise ValueError(f"El rol '{role}' no es válido. Debe ser uno de: {', '.join(dict(User.ROLES).keys())}")

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            role=role_normalizado,  # usamos la versión minúscula
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, first_name, last_name, role='administrador', password=None, **extra_fields):
        """
        Crea y guarda un superusuario. Por defecto usaremos role='administrador'.
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError("El superusuario debe tener is_staff=True.")
        if extra_fields.get('is_superuser') is not True:
            raise ValueError("El superusuario debe tener is_superuser=True.")

        # Normalizamos role a minúsculas para evitar errores de mayúsculas
        return self.create_user(email, first_name, last_name, role.lower(), password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    """
    Modelo de Usuario personalizado:
    - Se identifica por correo en lugar de username.
    - Incluye nombre, apellidos, rol, activo/inactivo, fechas de creación y último acceso.
    """
    ROLES = [
        ('administrador', 'Administrador'),
        ('dentista',      'Dentista'),
        ('recepcionista','Recepcionista'),
        ('paciente',      'Paciente'),
        ('laboratorio',   'Laboratorio'),
    ]

    email = models.EmailField('Correo Electrónico', unique=True)
    first_name = models.CharField('Nombres', max_length=30)
    last_name = models.CharField('Apellidos', max_length=30)
    role = models.CharField(
        'Rol',
        max_length=20,
        choices=ROLES,
        default='paciente',        # valor interno en minúsculas
    )
    is_active = models.BooleanField('¿Activo?', default=True)
    is_staff = models.BooleanField('¿Puede ingresar al admin?', default=False)
    date_joined = models.DateTimeField('Fecha de unión', auto_now_add=True)
    last_login = models.DateTimeField('Último acceso', auto_now=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'role']

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'

    def __str__(self):
        return f"{self.email} ({self.get_role_display()})"
