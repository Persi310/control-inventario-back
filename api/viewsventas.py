from django.views import View
from .models import Venta, DetalleVentas
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json

class VistaVentas(View):
    
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
            marcas = list (Venta.objects.filter(id=id).values())
            if(len(marcas) > 0):
                datos = {'message' : 'Successfully', 'marcas' : marcas}
            else:
                datos = {'message' : 'Venta no existente'}
            return JsonResponse(datos)    
        else:
            marcas = list (Venta.objects.values())                 
            if len(marcas) > 0 : 
                datos = {'message' : 'Successfully', 'marcas' : marcas}
            else: 
                datos = {'message' : 'Ventas no existentes'}
            return JsonResponse(datos) 
    def post(self, request):
        
        """ token = request.COOKIES.get('jwt')

        if not token:
             return JsonResponse({
                  "message" : "Usuario Inautenticado"
             }) """
             
        jd = json.loads(request.body)
        total = 0
        venta = Venta.objects.create(
            fecha=jd['fecha'],
            monto_total=total,
            usuario_id=jd['usuario_id'],
        )
        productos = jd.get('productos', [])
        for producto in productos:
            subtotal = producto['cantidad'] * producto['precio_unitario']
            DetalleVentas.objects.create(
                venta=venta,
                producto_id=producto['producto_id'],
                cantidad=producto['cantidad'],
                subtotal=subtotal,
                precio_unitario=producto['precio_unitario'],
            )
            total += subtotal
        venta.monto_total = total
        venta.save()

        datos = {'message': 'Successfully'}
        return JsonResponse(datos)
    def put(self, id):
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 
    def delete(self, id):
            jd = json.loads(id)
            Venta.objects.delete(jd)
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 