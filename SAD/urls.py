"""
URL configuration for SAD project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

# Importa la vista que renderiza primera_vista.html
from bienvenido import views as bienvenido_views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Ruta raíz → primera_vista
    # Al ir a http://127.0.0.1:8000/ cargará primera_vista.html
    path('', bienvenido_views.primera_vista, name='primera_vista'),
    
    # Aquí incluimos todas las URLs que empiecen con /accounts/
    path('accounts/', include('usuarios.urls', namespace='usuarios')),
    
    # Ahora montamos la app "bienvenido" en /bienvenido/
    path('bienvenido/', include('bienvenido.urls', namespace='bienvenido')),
    
    # App “doctores” en /doctores/
    path('doctores/', include('doctores.urls', namespace='doctores')),
    

    # Si luego agregas otras apps, las incluirías igual:
    # path('citas/', include('citas.urls', namespace='citas')),
    # path('pacientes/', include('pacientes.urls', namespace='pacientes')),
    # etc.
]
