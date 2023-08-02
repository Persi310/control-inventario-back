from django.views import View
from .models import Venta
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class VistaVentas(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if(id>0):
            marcas = list (Venta.objects.filter(id=id).values())
            if(len(marcas) > 0):
                datos = {'message' : 'Successfully', 'marcas' : marcas}
            else:
                datos = {'message' : 'Venta no existente'}
            return JsonResponse(datos)    
        else:
            marcas = list (Venta.objects.values())                 
            if len(marcas) > 0 : 
                datos = {'message' : 'Successfully', 'marcas' : marcas}
            else: 
                datos = {'message' : 'Ventas no existentes'}
            return JsonResponse(datos) 
    def post(self, request):
            jd = json.loads(request.body)
            Venta.objects.create(
              fecha = jd['fecha'],
              monto_total = jd['monto_total'],
              usuario_id = jd['usuario_id'],
            )
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 
    def put(self, id):
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 
    def delete(self, id):
            jd = json.loads(id)
            Venta.objects.delete(jd)
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 