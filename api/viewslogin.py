from django.views import View
from django.http.response import JsonResponse
from .models import Users
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
import jwt, datetime

class VistaLogin(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request):
        jd = json.loads(request.body)
        email = jd.get('email')
        password = jd.get('password')

        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            return JsonResponse({
                "message": "El usuario no existe"
            })

        if user.password != password:
            return JsonResponse({
                "message": "Contraseña incorrecta"
            })

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=120),
            'iat': datetime.datetime.utcnow()
        }

        secret_key = 'your_secret_key' 
        token = jwt.encode(payload, secret_key, algorithm='HS256')

        response = JsonResponse({
            "token": token
        })

        response.set_cookie(key='jwt', value=token, httponly=True)


        return response
    
class VistaLogout(View):
      
      @method_decorator(csrf_exempt)
      def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
      def post(self, request):

        response = JsonResponse({
            "message": "succes"
        })

        response.delete_cookie('jwt')

        return response