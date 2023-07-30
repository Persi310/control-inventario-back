from django.views import View
from .models import Rol
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class VistaRol(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if(id>0):
            roles = list (Rol.objects.filter(id=id).values())
            if(len(roles) > 0):
                datos = {'message' : 'Successfully', 'roles' : roles}
            else:
                datos = {'message' : 'Roles no existentes'}
            return JsonResponse(datos)    
        else:
            roles = list (Rol.objects.values())                 
            if len(roles) > 0 : 
                datos = {'message' : 'Successfully', 'roles' : roles}
            else: 
                datos = {'message' : 'Roles no existentes'}
            return JsonResponse(datos) 
    def post(self, request):
            jd = json.loads(request.body)
            Rol.objects.create(
              rol = jd['rol'],
            )
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 
    def put(self, id):
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 
    def delete(self, id):
            jd = json.loads(id)
            Rol.objects.delete(jd)
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 