from django.db import models

class Marca(models.Model):
    marca = models.CharField(max_length=150)