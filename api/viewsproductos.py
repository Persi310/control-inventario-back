from django.views import View
from .models import Producto
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class VistaProductos(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):

        """ token = request.COOKIES.get('jwt')

        if not token:
             return JsonResponse({
                  "message" : "Usuario Inautenticado"
             }) """

        if(id>0):
            productos = list (Producto.objects.filter(id=id).values())
            if(len(productos) > 0):
                datos = {'message' : 'Successfully', 'productos' : productos}
            else:
                datos = {'message' : 'Usuarios no existentes'}
            return JsonResponse(datos)    
        else:
            productos = list (Producto.objects.select_related('categoria', 'marca', 'proveedor').values('id', 'nombre', 'descripcion', 'precio', 'cantidad_minima', 'categoria__categoria', 'marca__marca', 'proveedor__first_name'))                 
            if len(productos) > 0 : 
                datos = {'message' : 'Successfully', 'productos' : list(productos)}
            else: 
                datos = {'message' : 'Usuarios no existentes'}
            return JsonResponse(datos) 
    def post(self, request):
        
        """ token = request.COOKIES.get('jwt')

        if not token:
             return JsonResponse({
                  "message" : "Usuario Inautenticado"
             }) """
             
        jd = json.loads(request.body)
        Producto.objects.create(
              nombre = jd['nombre'],
              descripcion = jd['descripcion'],
              precio = jd['precio'],
              cantidad_minima = jd['cantidad_minima'],
              categoria_id = jd['categoria_id'],
              marca_id = jd['marca_id'],
              proveedor_id = jd['proveedor_id'],
            )
        datos = {'message' : 'Successfully'}
        return JsonResponse(datos) 
    def put(self, request, id):
        try:
            print(request.body)  
            producto = Producto.objects.get(id=id)
            data = json.loads(request.body)
            print(data)  
            producto.nombre = data.get('nombre', producto.nombre)
            producto.descripcion = data.get('descripcion', producto.descripcion)
            producto.precio = data.get('precio', producto.precio)
            producto.cantidad_minima = data.get('cantidad_minima', producto.cantidad_minima)
            producto.save()
            datos = {'message': 'Producto actualizado correctamente'}
            return JsonResponse(datos) 
        except Producto.DoesNotExist:
            datos = {'message': 'Error'}
            return JsonResponse(datos) 
    def delete(self, request, id):
        marca_id = int(id)  # Convierte el ID a un entero (si es un string)
        try:
            marca = Producto.objects.get(id=marca_id)
            marca.delete()
            datos = {'message': 'Marca eliminada exitosamente'}
            return JsonResponse(datos)
        except Producto.DoesNotExist:
            datos = {'message': 'La marca no existe'}
            return JsonResponse(datos) 