from django.views import View
from .models import Users
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class VistaUsers(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):
        if(id>0):
            usuarios = list (Users.objects.filter(id=id).values())
            if(len(usuarios) > 0):
                datos = {'message' : 'Successfully', 'usuarios' : usuarios}
            else:
                datos = {'message' : 'Usuarios no existentes'}
            return JsonResponse(datos)    
        else:
            usuarios = list (Users.objects.values())                 
            if len(usuarios) > 0 : 
                datos = {'message' : 'Successfully', 'usuarios' : usuarios}
            else: 
                datos = {'message' : 'Usuarios no existentes'}
            return JsonResponse(datos) 
    def post(self, request):
            jd = json.loads(request.body)
            Users.objects.create(
              nombre_usuario = jd['nombre_usuario'],
              correo_electronico = jd['correo_electronico'],
              password = jd['password'],
              primer_nombre = jd['primer_nombre'],
              segundo_nombre = jd['segundo_nombre'],
              primer_apellido = jd['primer_apellido'],
              segundo_apellido = jd['segundo_apellido'],
              direccion = jd['direccion'],
              telefono = jd['telefono'],
              nombre_empresa = jd['nombre_empresa'],
              rol_id = jd['rol_id'],
            )
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 
    def put(self, id):
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 
    def delete(self, id):
            jd = json.loads(id)
            Users.objects.delete(jd)
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 