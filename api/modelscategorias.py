from django.db import models

class Categoria(models.Model):
    categoria = models.CharField(max_length=150)  