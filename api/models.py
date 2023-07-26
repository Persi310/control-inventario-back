from django.db import models

class Proveedores(models.Model):
    proveedor = models.CharField(max_length= 50)
