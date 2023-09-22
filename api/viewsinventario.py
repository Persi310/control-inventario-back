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

        if(id>0):
            marcas = list (Inventario.objects.filter(id=id).values())
            if(len(marcas) > 0):
                datos = {'message' : 'Successfully', 'marcas' : marcas}
            else:
                datos = {'message' : 'Inventario sin stock'}
            return JsonResponse(datos)    
        else:
            marcas = list (Inventario.objects.values())                 
            if len(marcas) > 0 : 
                datos = {'message' : 'Successfully', 'marcas' : marcas}
            else: 
                datos = {'message' : 'Inventario sin stock'}
            return JsonResponse(datos) 
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
    def put(self, id):
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 
    def delete(self, id):
            jd = json.loads(id)
            Inventario.objects.delete(jd)
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 