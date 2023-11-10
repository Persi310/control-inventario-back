from django.views import View
from .models import Venta, DetalleVentas, Inventario
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from django.db.models import Sum
from django.http import HttpResponse

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
        if request.path.endswith('/top5'):
            return self.get_top_5_products(request)
        else:
            if(id>0):
                marcas = list (Venta.objects.filter(id=id).values())
                if(len(marcas) > 0):
                    datos = {'message' : 'Successfully', 'ventas' : marcas}
                else:
                    datos = {'message' : 'Venta no existente'}
                return JsonResponse(datos)    
            else:
                marcas = list (Venta.objects.select_related('usuario').values('id', 'fecha', 'monto_total', 'usuario__first_name'))                 
                if len(marcas) > 0 : 
                    datos = {'message' : 'Successfully', 'ventas' : marcas}
                else: 
                    datos = {'message' : 'Ventas no existentes'}
                return JsonResponse(datos)
    pass 
    def post(self, request):
        try:
            data = json.loads(request.body)
            compra_data = data.get('venta', {})
            fecha = compra_data.get('fecha', '')
            usuario_id = compra_data.get('usuario_id', '')
            productos = compra_data.get('productos', [])

            nueva_compra = Venta.objects.create(fecha=fecha, usuario_id=usuario_id, monto_total=0)

            total_compra = 0

            for producto_data in productos:
                producto_id = producto_data.get('producto_id')
                cantidad = producto_data.get('cantidad')
                precio = producto_data.get('precio')

                DetalleVentas.objects.create(
                    venta=nueva_compra,
                    producto_id=producto_id,
                    cantidad=cantidad,
                    subtotal = cantidad * precio,
                    precio_unitario=precio
                )

                fecha_actual = datetime.now()
                producto = Inventario.objects.get(id=producto_id)
                producto.cantidad_stock -= cantidad
                producto.fecha_ultima_actualizacion = fecha_actual
                producto.tienda_id = 1
                producto.save()

                subtotal = cantidad * precio
                total_compra += subtotal  # Sumar el subtotal al total de la compra

            nueva_compra.monto_total = total_compra  # Asignar el total al modelo Compra
            nueva_compra.save()

            response_data = {
                'message': 'Compra creada exitosamente.'
            }
        except Exception as e:
            response_data = {
                'message': 'Error en el servidor al procesar los datos: {}'.format(str(e))
            }
        return JsonResponse(response_data)
    def put(self, id):
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 
    def delete(self, id):
            jd = json.loads(id)
            Venta.objects.delete(jd)
            datos = {'message' : 'Successfully'}
            return JsonResponse(datos) 
        
    def get_top_5_products(self, request):
        try:
            top_products = (
                DetalleVentas.objects
                .values('producto__id', 'producto__nombre')  # Seleccionar ID y nombre del producto
                .annotate(total_cantidad=Sum('cantidad'))  # Sumar la cantidad vendida por producto
                .order_by('-total_cantidad')[:5]  # Obtener los 5 productos con mayor cantidad vendida
            )

            top_products_list = list(top_products)
            response_data = {
                'message': 'Top 5 productos con mayor cantidad vendida',
                'top_products': top_products_list
            }

            return JsonResponse(response_data)
        except Exception as e:
            response_data = {
                'message': 'Error al obtener los 5 productos: {}'.format(str(e))
            }
            return JsonResponse(response_data, status=500)