# usuarios/forms.py

from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class UserRegistrationForm(UserCreationForm):
    """
    Formulario público para que solamente se puedan registrar Pacientes.
    Forzamos role='Paciente' en save().
    """
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        ]
        labels = {
            'email': 'Correo Electrónico',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
        }

    def save(self, commit=True):
        """
        Cuando alguien use el signup público y llene este formulario,
        este método forzará que role = 'Paciente' antes de guardar.
        """
        user = super().save(commit=False)
        user.role = 'paciente'
        if commit:
            user.save()
        return user


class UserEditForm(UserChangeForm):
    """
    Formulario para que el paciente edite SU propio perfil.
    NO incluye el campo 'role'.
    """
    password = None  # Ocultar el campo de contraseña

    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
        ]
        labels = {
            'email': 'Correo Electrónico',
            'first_name': 'Nombres',
            'last_name': 'Apellidos',
        }


class UserAdminCreationForm(UserCreationForm):
    """
    Formulario para crear usuarios desde el Admin, donde sí se puede elegir 'role'.
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

    def save(self, commit=True):
        user = super().save(commit=False)
        # Si lo guardas con commit=True, se guarda con el role que el Admin seleccionó
        if commit:
            user.save()
        return user


class UserAdminForm(UserChangeForm):
    """
    Formulario para EDITAR usuarios desde el Admin, que sí incluye 'role'.
    """
    class Meta:
        model = User
        fields = [
            'email',
            'first_name',
            'last_name',
            'role',
            'is_staff',
            'is_active',
            'is_superuser',
        ]
