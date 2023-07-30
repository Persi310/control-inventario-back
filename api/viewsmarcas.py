from django.views import View
from .models import Marca
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class VistaMarcas(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if(id>0):
            marcas = list (Marca.objects.filter(id=id).values())
            if(len(marcas) > 0):
                datos = {'message' : 'Successfully', 'marcas' : marcas}
            else:
                datos = {'message' : 'Marcas no existentes'}
            return JsonResponse(datos)    
        else:
            marcas = list (Marca.objects.values())                 
            if len(marcas) > 0 : 
                datos = {'message' : 'Successfully', 'marcas' : marcas}
            else: 
                datos = {'message' : 'Marcas no existentes'}
            return JsonResponse(datos) 
    def post(self, request):
            jd = json.loads(request.body)
            Marca.objects.create(
              marca = jd['marca'],
            )
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 
    def put(self, id):
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 
    def delete(self, id):
            jd = json.loads(id)
            Marca.objects.delete(jd)
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 