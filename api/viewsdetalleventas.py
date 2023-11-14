from django.views import View
from .models import Compra, DetalleVentas, Inventario
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from datetime import datetime

class VistaDetalleVentas(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self, request, venta_id):
        detalles = DetalleVentas.objects.filter(venta_id=venta_id).select_related('producto').values('producto__nombre', 'cantidad', 'precio_unitario')
        
        detalles_list = list(detalles)
        if detalles_list:
            response_data = {
                'message': 'Detalles de la venta obtenidos exitosamente.',
                'detalles_venta': detalles_list
            }
        else:
            response_data = {
                'message': 'No se encontraron detalles para la venta especificada.'
            }

        return JsonResponse(response_data)