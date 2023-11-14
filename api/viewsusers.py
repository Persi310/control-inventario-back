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
    def put(self, request, id):
        try:
            user = Users.objects.get(id=id)  # Obtén el usuario a actualizar
            jd = json.loads(request.body)  # Obtén los datos del cuerpo de la solicitud
            user.is_superuser = jd.get('is_superuser', user.is_superuser)
            user.username = jd.get('username', user.username)
            user.first_name = jd.get('first_name', user.first_name)
            user.last_name = jd.get('last_name', user.last_name)
            user.is_staff = jd.get('is_staff', user.is_staff)
            user.is_active = jd.get('is_active', user.is_active)
            user.date_joined = jd.get('date_joined', user.date_joined)
            user.email = jd.get('email', user.email)
            user.password = jd.get('password', user.password)
            user.direccion = jd.get('direccion', user.direccion)
            user.telefono = jd.get('telefono', user.telefono)
            user.nombre_empresa = jd.get('nombre_empresa', user.nombre_empresa)

            user.save()  # Guarda los cambios

            datos = {'message': 'Usuario actualizado correctamente'}
            return JsonResponse(datos)
        except Users.DoesNotExist:
            datos = {'message': 'El usuario no existe'}
            return JsonResponse(datos)
    def delete(self, request, id):
        marca_id = int(id)  # Convierte el ID a un entero (si es un string)
        try:
            marca = Users.objects.get(id=marca_id)
            marca.delete()
            datos = {'message': 'Marca eliminada exitosamente'}
            return JsonResponse(datos)
        except Users.DoesNotExist:
            datos = {'message': 'La marca no existe'}
            return JsonResponse(datos)