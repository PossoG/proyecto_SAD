# core/urls.py

from django.urls import path
from .views import HomeView  # O home_redirect si eliges la redirección

app_name = 'core'  # namespace para las URLs de core

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # Si hubieras usado la función de redirect:
    # path('', home_redirect, name='home'),
]
