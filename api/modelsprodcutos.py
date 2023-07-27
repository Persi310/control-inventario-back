from django.db import models

class Producto(models.Model):
    producto = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.FloatField()
    cantidad = models.IntegerField()