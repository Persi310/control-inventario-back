from django.views import View
from .models import Categoria
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class VistaCategorias(View):
    
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
            categorias = list (Categoria.objects.filter(id=id).values())
            if(len(categorias) > 0):
                datos = {'message' : 'Successfully', 'categorias' : categorias}
            else:
                datos = {'message' : 'Categorias no existentes'}
            return JsonResponse(datos)    
        else:
            categorias = list (Categoria.objects.values())                 
            if len(categorias) > 0 : 
                datos = {'message' : 'Successfully', 'categorias' : categorias}
            else: 
                datos = {'message' : 'Categorias no existentes'}
            return JsonResponse(datos) 
    def post(self, request):
        
        """ token = request.COOKIES.get('jwt')

        if not token:
             return JsonResponse({
                  "message" : "Usuario Inautenticado"
             }) """
               
        jd = json.loads(request.body)
            
        Categoria.objects.create(
              categoria = jd['categoria'],
            )
        datos = {'message' : 'Successfully'}
        return JsonResponse(datos) 
    def put(self, request,  id):
        
        """ token = request.COOKIES.get('jwt')

        if not token:
             return JsonResponse({
                  "message" : "Usuario Inautenticado"
             }) """
        
        jd = json.loads(request.body)
        categorias = list (Categoria.objects.filter(id=id).values())
        if(len(categorias) > 0):
                categoria=Categoria.objects.get(id=id)
                categoria.categoria = jd['categoria']
                categoria.save()
                datos = {'message' : 'Successfully'}
        else:
                datos = {'message' : 'Categorias no existentes'}     
        return JsonResponse(datos) 
    
    def delete(self, request, id):
        
        """ token = request.COOKIES.get('jwt')

        if not token:
             return JsonResponse({
                  "message" : "Usuario Inautenticado"
             }) """
        categorias = list (Categoria.objects.filter(id=id).values())
        if(len(categorias) > 0):
                Categoria.objects.filter(id=id).delete()
                datos = {'message' : 'Successfully'}
        else:
                datos = {'message' : 'Categorias no existentes'}     
        return JsonResponse(datos)  