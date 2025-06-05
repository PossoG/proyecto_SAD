from django.urls import path
from . import views

app_name = 'pacientes'

urlpatterns = [
    path('mis_historias/', views.mis_historias, name='mis_historias'),
    path('historia/<int:pk>/', views.detalle_historia, name='detalle_historia'),
    path('historia/<int:historia_pk>/agregar_procedimiento/', views.agregar_procedimiento, name='agregar_procedimiento'),
    # Si quisieras editar o borrar un procedimiento, crearías rutas adicionales:
    # path('procedimiento/<int:pk>/editar/', views.editar_procedimiento, name='editar_procedimiento'),
    # path('procedimiento/<int:pk>/eliminar/', views.eliminar_procedimiento, name='eliminar_procedimiento'),
]
