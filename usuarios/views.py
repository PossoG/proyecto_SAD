# usuarios/views.py

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from .models import User
from .forms import UserRegistrationForm, UserEditForm

class SignUpView(CreateView):
    """
    Vista para registrar un nuevo usuario.
    (En este momento la plantilla puede estar vacía o no existir aún, pero 
     definimos la clase para que el servidor no dé error. 
     Luego, cuando hagas signup.html, la sujetará aquí.)
    """
    model = User
    form_class = UserRegistrationForm
    template_name = 'usuarios/signup.html'   # luego crearás este archivo

    # Si quieres, por ahora indicamos un success_url que simplemente vuelva al login
    success_url = reverse_lazy('usuarios:login')


class LoginView(DjangoLoginView):
    """
    Hereda de DjangoLoginView. 
    En esta fase la plantilla puede no existir aún. Se define para que Django arranque.
    """
    template_name = 'usuarios/login.html'    # luego crearás este archivo
    redirect_authenticated_user = True


class LogoutView(DjangoLogoutView):
    """
    Hereda de DjangoLogoutView. 
    Cuando alguien cierre sesión, lo mandamos al login.
    """
    next_page = reverse_lazy('usuarios:login')


class UserEditView(UpdateView):
    """
    Vista para que el usuario edite su propio perfil.
    La plantilla aún no existe, pero la definimos para no romper urls.
    """
    model = User
    form_class = UserEditForm
    template_name = 'usuarios/profile_edit.html'   # luego crearás este archivo
    success_url = reverse_lazy('core:home')         # asume que tienes una app "core" con ruta "home"

    def get_object(self, queryset=None):
        # Siempre retorna al usuario en sesión
        return self.request.user


class UserDeleteView(DeleteView):
    """
    Vista para "eliminar" (en realidad desactivar) la cuenta del usuario.
    """
    model = User
    template_name = 'usuarios/profile_confirm_delete.html'  # luego crearás este archivo
    success_url = reverse_lazy('core:home')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        user = self.get_object()
        user.is_active = False
        user.save()
        return super().delete(request, *args, **kwargs)
