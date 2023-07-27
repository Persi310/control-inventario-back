from django.urls import path
from .views import VistaUsers

urlpatterns = [
    path('users', VistaUsers.as_view(), name='lista_usuarios'),
    path('users/<int:id>', VistaUsers.as_view(), name='procesos_usuarios'),
]