from django.views import View
from .models import Tienda
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class VistaTiendas(View):
    
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
            tiendas = list (Tienda.objects.filter(id=id).values())
            if(len(tiendas) > 0):
                datos = {'message' : 'Successfully', 'marcas' : tiendas}
            else:
                datos = {'message' : 'Tienda no existente'}
            return JsonResponse(datos)    
        else:
            tiendas = list (Tienda.objects.values())                 
            if len(tiendas) > 0 : 
                datos = {'message' : 'Successfully', 'tiendas' : tiendas}
            else: 
                datos = {'message' : 'Tienda no existente'}
            return JsonResponse(datos) 
    def post(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
             return JsonResponse({
                  "message" : "Usuario Inautenticado"
             })
        jd = json.loads(request.body)
        Tienda.objects.create(
              tienda = jd['tienda'],
              direccion = jd['direccion'],
            )
        datos = {'message' : 'Successfully'}
        return JsonResponse(datos) 
    def put(self, id):
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 
    def delete(self, id):
            jd = json.loads(id)
            Tienda.objects.delete(jd)
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 