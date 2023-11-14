from django.views import View
from .models import Inventario
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class VistaInventario(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):

        """ token = request.COOKIES.get('jwt')

        if not token:
             return JsonResponse({
                  "message" : "Usuario Inautenticado"
             }) """
        if request.path.endswith('/top5'):
            return self.obtener_productos_poco_stock(request)
        else:
            if(id>0):
                marcas = list (Inventario.objects.filter(id=id).values())
                if(len(marcas) > 0):
                    datos = {'message' : 'Successfully', 'inventario' : marcas}
                else:
                    datos = {'message' : 'Inventario sin stock'}
                return JsonResponse(datos)    
            else:
                marcas = list (Inventario.objects.select_related('producto', 'tienda').values('id', 'cantidad_stock', 'fecha_ultima_actualizacion', 'producto__nombre', 'tienda__tienda'))                 
                if len(marcas) > 0 : 
                    datos = {'message' : 'Successfully', 'inventario' : marcas}
                else: 
                    datos = {'message' : 'Inventario sin stock'}
                return JsonResponse(datos) 
    pass
    def post(self, request):
        """ token = request.COOKIES.get('jwt')

        if not token:
             return JsonResponse({
                  "message" : "Usuario Inautenticado"
             }) """
             
        jd = json.loads(request.body)
        Inventario.objects.create(
              cantidad_stock = jd['cantidad_stock'],
              fecha_ultima_actualizacion = jd['fecha_ultima_actualizacion'],
              producto_id = jd['producto_id'],
              tienda_id = jd['tienda_id'],
            )
        datos = {'message' : 'Successfully'}
        return JsonResponse(datos) 
    
    def obtener_productos_poco_stock(self, request):
        try:
            productos_poco_stock = Inventario.objects.filter(cantidad_stock__lt=100).values('producto__nombre', 'cantidad_stock', 'fecha_ultima_actualizacion', 'tienda__tienda')
            top_products_list = list(productos_poco_stock)
            response_data = {
                'message': 'Top 5 productos con menor stock',
                'top_products': top_products_list
            }
            return JsonResponse(response_data)
        except Exception as e:
            response_data = {
                'message': 'Error al obtener los 5 productos: {}'.format(str(e))
            }
            return JsonResponse(response_data, status=500)
    