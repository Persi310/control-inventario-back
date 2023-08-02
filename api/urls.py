from django.urls import path
from .viewsusers import VistaUsers
from .viewscategorias import VistaCategorias
from .viewsmarcas import VistaMarcas
from .viewsproductos import VistaProductos
from .viewsrol import VistaRol
from .viewscompra import VistaCompras
from .viewsinventario import VistaInventario
from .viewstiendas import VistaTiendas
from .viewsventas import VistaVentas


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

    #RUTAS ROLES
    path('rol', VistaRol.as_view(), name='lista_roles'),
    path('rol/<int:id>', VistaRol.as_view(), name='procesos_roles'),

    #RUTAS COMPRAS
    path('compras', VistaCompras.as_view(), name='lista_compras'),
    path('compras/<int:id>', VistaCompras.as_view(), name='procesos_compras'),

    #RUTAS Inventario
    path('inventario', VistaInventario.as_view(), name='lista_inventario'),
    path('inventario/<int:id>', VistaInventario.as_view(), name='procesos_inventario'),

    #RUTAS Tiendas
    path('tiendas', VistaTiendas.as_view(), name='lista_tiendas'),
    path('tiendas/<int:id>', VistaTiendas.as_view(), name='procesos_tiendas'),

    #RUTAS Ventas
    path('ventas', VistaVentas.as_view(), name='lista_ventas'),
    path('ventas/<int:id>', VistaVentas.as_view(), name='procesos_ventas'),
]