from django.views import View
from .models import Compra, DetalleCompras
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class VistaCompras(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, id=0):

        token = request.COOKIES.get('jwt')

        if not token:
             return JsonResponse({
                  "message" : "Usuario Inautenticado"
             })

        if(id>0):
            compras = list (Compra.objects.filter(id=id).values())
            if(len(compras) > 0):
                datos = {'message' : 'Successfully', 'compras' : compras}
            else:
                datos = {'message' : 'Compras no existentes'}
            return JsonResponse(datos)    
        else:
            compras = list (Compra.objects.values())                 
            if len(compras) > 0 : 
                datos = {'message' : 'Successfully', 'categorias' : compras}
            else: 
                datos = {'message' : 'Compras no existentes'}
            return JsonResponse(datos) 
    def post(self, request):
        
        token = request.COOKIES.get('jwt')

        if not token:
             return JsonResponse({
                  "message" : "Usuario Inautenticado"
             })
             
        jd = json.loads(request.body)
        total = 0
        compra = Compra.objects.create(
            fecha=jd['fecha'],
            total=0,
            usuario_id=jd['usuario_id'],
        )
        productos = jd.get('productos', [])
        for producto in productos:
            subtotal = producto['cantidad'] * producto['precio_unitario']
            DetalleCompras.objects.create(
                compra=compra,
                producto_id=producto['producto_id'],
                cantidad=producto['cantidad'],
                subtotal=subtotal,
                precio_unitario=producto['precio_unitario'],
            )
            total += subtotal

        compra.total = total
        compra.save()

        datos = {'message': 'Successfully'}
        return JsonResponse(datos) 
    def put(self, id):
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 
    def delete(self, id):
            jd = json.loads(id)
            Compra.objects.delete(jd)
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 