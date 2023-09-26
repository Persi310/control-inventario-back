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
        """ token = request.COOKIES.get('jwt')

        if not token:
             return JsonResponse({
                  "message" : "Usuario Inautenticado"
             }) """
        
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
              is_superuser = jd['is_superuser'],
              username = jd['username'],
              first_name = jd['first_name'],
              last_name = jd['last_name'],
              is_staff = jd['is_staff'],
              is_active = jd['is_active'],
              date_joined = jd['date_joined'],
              email = jd['email'],
              password = jd['password'],
              direccion = jd['direccion'],
              telefono = jd['telefono'],
              nombre_empresa = jd['nombre_empresa'],
              rol_id = 1,
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