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

        """ token = request.COOKIES.get('jwt')

        if not token:
             return JsonResponse({
                  "message" : "Usuario Inautenticado"
             }) """

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
        """ token = request.COOKIES.get('jwt')

        if not token:
             return JsonResponse({
                  "message" : "Usuario Inautenticado"
             })
              """
        jd = json.loads(request.body)
        Marca.objects.create(
              marca = jd['marca'],
            )
        datos = {'message' : 'Successfully'}
        return JsonResponse(datos) 
    def put(self, request, id):
        try:
            marca = Marca.objects.get(id=id)
            data = json.loads(request.body)
            marca.marca = data.get('marca', marca.marca)
            marca.save()
            datos = {'message': 'Marca actualizada correctamente'}
            return JsonResponse(datos) 
        except Marca.DoesNotExist:
            datos = {'message': 'Error'}
            return JsonResponse(datos) 
    def delete(self, request, id):
        marca_id = int(id)  # Convierte el ID a un entero (si es un string)
        try:
            marca = Marca.objects.get(id=marca_id)
            marca.delete()
            datos = {'message': 'Marca eliminada exitosamente'}
            return JsonResponse(datos)
        except Marca.DoesNotExist:
            datos = {'message': 'La marca no existe'}
            return JsonResponse(datos)