# usuarios/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    """
    Formulario para registrar un nuevo usuario.
    Incluye validación automática de contraseña (dos veces).
    """
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'role',
            'password1',
            'password2',
        ]
        labels = {
            'email': 'Correo Electrónico',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'role': 'Rol',
        }

class UserEditForm(UserChangeForm):
    """
    Formulario para editar datos del usuario (excepto contraseña).
    Oculta el campo password.
    """
    password = None  # No mostrar el campo contraseña en el formulario de edición

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'role',
        ]
        labels = {
            'email': 'Correo Electrónico',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
            'role': 'Rol',
        }
