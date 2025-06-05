# usuarios/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User
from .forms import (
    UserRegistrationForm,
    UserAdminCreationForm,
    UserAdminForm,
)

@admin.register(User)

class UserAdmin(DjangoUserAdmin):
    add_form = UserAdminCreationForm
    form = UserAdminForm
    model = User

    list_display = ('email', 'first_name', 'last_name', 'role', 'is_staff', 'is_active')
    list_filter = ('role', 'is_staff', 'is_active')

    # Declaro last_login y date_joined como campos de solo lectura
    readonly_fields = ('last_login', 'date_joined')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Información Personal', {'fields': ('first_name', 'last_name', 'role')}),
        ('Permisos', {'fields': ('is_staff', 'is_active', 'is_superuser', 'groups', 'user_permissions')}),
        # En esta sección solo mostramos los campos de solo lectura
        ('Información de acceso', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'role',
                'password1',
                'password2',
                'is_staff',
                'is_active',
            )
        }),
    )

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)

    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
