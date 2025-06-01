# usuarios/views.py

from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.views import LoginView as DjangoLoginView, LogoutView as DjangoLogoutView
from .models import User
from .forms import UserRegistrationForm, UserEditForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect



class SignUpView(CreateView):
    model = User
    form_class = UserRegistrationForm   # ← Aquí debe apuntar a UserRegistrationForm
    template_name = 'usuarios/signup.html'
    success_url = reverse_lazy('usuarios:login')


class LoginView(DjangoLoginView):
    template_name = 'usuarios/login.html'
    redirect_authenticated_user = True


class LogoutView(DjangoLogoutView):
    next_page = reverse_lazy('usuarios:login')


class UserEditView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserEditForm
    template_name = 'usuarios/profile_edit.html'
    success_url = reverse_lazy('core:home')

    def get_object(self, queryset=None):
        # Solo el usuario en sesión puede editarse a sí mismo
        return self.request.user


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    template_name = 'usuarios/profile_confirm_delete.html'
    success_url = reverse_lazy('core:home')
    context_object_name = 'user'

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        """
        En lugar de eliminar físicamente, marcamos `is_active=False`
        y redirigimos al home.
        """
        user = self.get_object()
        user.is_active = False
        user.save()
        return redirect(self.success_url)
