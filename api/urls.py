from django.urls import path
from .viewsusers import VistaUsers
from .viewscategorias import VistaCategorias
from .viewsmarcas import VistaMarcas
from .viewsproductos import VistaProductos

urlpatterns = [

    #RUTAS USERS
    path('users', VistaUsers.as_view(), name='lista_usuarios'),
    path('users/<int:id>', VistaUsers.as_view(), name='procesos_usuarios'),

    #RUTAS MARCAS 
    path('marcas', VistaMarcas.as_view(), name='lista_marcas'),
    path('marcas/<int:id>', VistaMarcas.as_view(), name='procesos_marcas'),

    #RUTAS CATEGORIAS
    path('categorias', VistaCategorias.as_view(), name='lista_categorias'),
    path('categorias/<int:id>', VistaCategorias.as_view(), name='procesos_categorias'),

    #RUTAS PRODCUTOS
    path('productos', VistaProductos.as_view(), name='lista_productos'),
    path('productos/<int:id>', VistaProductos.as_view(), name='procesos_prodcutos'),
]