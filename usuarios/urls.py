# usuarios/urls.py

from django.urls import path
from . import views

# Namespace para referenciar las rutas desde plantillas
app_name = 'usuarios'

urlpatterns = [
    path('signup/', views.SignUpView.as_view(),      name='signup'),
    path('login/',  views.LoginView.as_view(),       name='login'),
    path('logout/', views.LogoutView.as_view(),      name='logout'),
    path('profile/edit/',   views.UserEditView.as_view(),   name='profile_edit'),
    path('profile/delete/', views.UserDeleteView.as_view(), name='profile_delete'),
]
