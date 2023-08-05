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

        token = request.COOKIES.get('jwt')

        if not token:
             return JsonResponse({
                  "message" : "Usuario Inautenticado"
             })

        if(id>0):
            usuarios = list (Producto.objects.filter(id=id).values())
            if(len(usuarios) > 0):
                datos = {'message' : 'Successfully', 'usuarios' : usuarios}
            else:
                datos = {'message' : 'Usuarios no existentes'}
            return JsonResponse(datos)    
        else:
            usuarios = list (Producto.objects.values())                 
            if len(usuarios) > 0 : 
                datos = {'message' : 'Successfully', 'usuarios' : usuarios}
            else: 
                datos = {'message' : 'Usuarios no existentes'}
            return JsonResponse(datos) 
    def post(self, request):
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
    def put(self, id):
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 
    def delete(self, id):
            jd = json.loads(id)
            Producto.objects.delete(jd)
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 