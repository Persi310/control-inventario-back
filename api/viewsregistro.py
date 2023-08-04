from django.views import View
from .models import Users
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class VistaRegistro(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
            jd = json.loads(request.body)
            Users.objects.create(
              username = jd['username'],
              is_superuser = jd['is_superuser'],
              email = jd['email'],
              password = jd['password'],
              first_name = jd['first_name'],
              last_name = jd['last_name'],
              is_staff = jd['is_staff'],
              is_active = jd['is_active'],
              date_joined = jd['date_joined'],
              direccion = jd['direccion'],
              telefono = jd['telefono'],
              nombre_empresa = jd['nombre_empresa'],
              rol_id = jd['rol_id'],
            )
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 