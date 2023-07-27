from django.contrib import admin
from .modelscategorias import Categoria
from .modelsmarcas import Marca
from .modelsprodcutos import Producto
from .modelsusers import Users

admin.site.register(Users)
admin.site.register(Categoria)
admin.site.register(Marca)
admin.site.register(Producto)
