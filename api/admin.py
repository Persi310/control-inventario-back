from django.contrib import admin
from .models import Users, Producto, Categoria, Marca, Tienda, DetalleCompras, Compra, Venta, Rol, DetalleVentas, Inventario

admin.site.register(Users)
admin.site.register(Producto)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Tienda)
admin.site.register(DetalleCompras)
admin.site.register(Compra)
admin.site.register(Venta)
admin.site.register(Rol)
admin.site.register(DetalleVentas)
admin.site.register(Inventario)