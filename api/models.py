from django.db import models

class Rol(models.Model):
    rol = models.CharField(max_length=150)

class Users(models.Model):
    nombre_usuario = models.CharField(max_length=150)
    correo_electronico = models.EmailField()
    password = models.CharField(max_length=150)
    primer_nombre = models.CharField(max_length=150)
    segundo_nombre = models.CharField(max_length=150)
    primer_apellido = models.CharField(max_length=150)
    segundo_apellido = models.CharField(max_length=150)
    direccion = models.TextField()
    telefono = models.IntegerField()
    nombre_empresa = models.CharField(max_length=150)
    rol = models.ForeignKey(Rol , on_delete=models.CASCADE)

class Categoria(models.Model):
    categoria = models.CharField(max_length=150)  

class Marca(models.Model):
    marca = models.CharField(max_length=150)

class Tienda(models.Model):
    tienda = models.CharField(max_length=150)
    direccion = models.TextField()

class Producto(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField()
    precio = models.FloatField()
    cantidad_minima = models.IntegerField()
    categoria = models.ForeignKey(Categoria , on_delete=models.CASCADE)
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    proveedor = models.ForeignKey(Users , on_delete=models.CASCADE)

class Inventario(models.Model):
    cantidad_stock = models.IntegerField()
    fecha_ultima_actualizacion = models.DateField()
    tienda = models.ForeignKey(Tienda , on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class Venta(models.Model):
    fecha = models.DateField()
    monto_total = models.FloatField()
    usuario = models.ForeignKey(Users, on_delete=models.CASCADE)

class Compra(models.Model):
    fecha = models.DateField()
    total = models.FloatField()
    usuario = models.ForeignKey(Users, on_delete=models.CASCADE)

class DetalleVentas(models.Model):
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()
    subtotal = models.FloatField()
    venta = models.ForeignKey(Venta , on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)

class DetalleCompras(models.Model):
    cantidad = models.IntegerField()
    precio_unitario = models.FloatField()
    subtotal = models.FloatField()
    compra = models.ForeignKey(Compra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
