from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'administradores/index.html')

def inventario_registrar(request):
    return render(request, 'administradores/inventario_registrar.html')

def inventario_alertas(request):
    return render(request, 'administradores/inventario_alertas.html')

def proveedores_registrar(request):
    return render(request, 'administradores/proveedor_registrar.html')