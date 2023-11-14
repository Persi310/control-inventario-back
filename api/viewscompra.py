from django.views import View
from .models import Compra, DetalleCompras, Inventario
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime
from django.db import transaction

class VistaCompras(View):
    
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
                compras = list (Compra.objects.filter(id=id).values())
                if(len(compras) > 0):
                    datos = {'message' : 'Successfully', 'compras' : compras}
                else:
                    datos = {'message' : 'Compras no existentes'}
                return JsonResponse(datos)    
        else:
                compras = list (Compra.objects.select_related('usuario').values('id', 'fecha', 'total', 'usuario__first_name'))                 
                if len(compras) > 0 : 
                    datos = {'message' : 'Successfully', 'compras' : compras}
                else: 
                    datos = {'message' : 'Compras no existentes'}
                return JsonResponse(datos) 
    def post(self, request):
        try:
            data = json.loads(request.body)
            compra_data = data.get('compra', {})
            fecha = compra_data.get('fecha', '')
            usuario_id = compra_data.get('usuario_id', '')
            productos = compra_data.get('productos', [])

            nueva_compra = Compra.objects.create(fecha=fecha, usuario_id=usuario_id, total=0)

            total_compra = 0

            for producto_data in productos:
                producto_id = producto_data.get('producto_id')
                cantidad = producto_data.get('cantidad')
                precio = producto_data.get('precio')

                DetalleCompras.objects.create(
                    compra=nueva_compra,
                    producto_id=producto_id,
                    cantidad=cantidad,
                    subtotal=cantidad * precio,
                    precio_unitario=precio
                )

                fecha_actual = datetime.now()

                # Buscar el producto en Inventario o crearlo si no existe
                producto, creado = Inventario.objects.get_or_create(id=producto_id, defaults={
                    'cantidad_stock': cantidad,
                    'producto_id': producto_id,
                    'fecha_ultima_actualizacion': fecha_actual,
                    'tienda_id': 1
                })

                # Actualizar la cantidad del producto si no se creó uno nuevo
                if not creado:
                    producto.cantidad_stock += cantidad
                    producto.fecha_ultima_actualizacion = fecha_actual
                    producto.tienda_id = 1
                    producto.save()

                subtotal = cantidad * precio
                total_compra += subtotal

            nueva_compra.total = total_compra
            nueva_compra.save()

            response_data = {
                'message': 'Compra creada exitosamente.'
            }
        except Exception as e:
            response_data = {
                'message': 'Error en el servidor al procesar los datos: {}'.format(str(e))
            }
        return JsonResponse(response_data)

    def obtener_productos(self, request, compra_id):
        detalles = DetalleCompras.objects.filter(compra_id=compra_id).values('producto_id', 'cantidad', 'precio_unitario')
        
        detalles_list = list(detalles)
        if detalles_list:
            response_data = {
                'message': 'Detalles de la compra obtenidos exitosamente.',
                'detalles_compra': detalles_list
            }
        else:
            response_data = {
                'message': 'No se encontraron detalles para la compra especificada.'
            }

        return JsonResponse(response_data)