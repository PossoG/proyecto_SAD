from django.shortcuts import render
from django.views.generic import TemplateView


# core/views.py
# Esta vista simplemente renderiza la plantilla 'core/home.html'
class HomeView(TemplateView):
    template_name = 'core/home.html'
