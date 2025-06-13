from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

#MODELOS RELACIONADOS AL USUARIOS
class rolUsuario(models.Model):
    idRol = models.AutoField(primary_key=True)
    nombreRol = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombreRol

class region(models.Model):
    idRegion = models.AutoField(primary_key=True)
    nombreRegion = models.CharField(max_length=80, blank=False, null=False)

    def __str__(self):
        return self.nombreRegion

class comuna(models.Model):
    idComuna = models.AutoField(primary_key=True)
    nombreComuna = models.CharField(max_length=80, blank=False, null=False)
    idRegion = models.ForeignKey(region, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreComuna

class usuarioCustom(AbstractUser):
    run = models.CharField(max_length=12, blank=False, null=False)
    pnombre = models.CharField(max_length=20, blank=False, null=False)
    snombre = models.CharField(max_length=20, blank=True)
    ap_paterno = models.CharField(max_length=24, blank=False, null=False)
    ap_materno = models.CharField(max_length=24, blank=True)
    correo_usuario = models.EmailField(blank=False, null=False)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    direccion = models.CharField(blank=False, null=False, max_length=100)
    idComuna = models.ForeignKey(comuna, on_delete=models.CASCADE, blank=True, null=True)
    idRol = models.ForeignKey(rolUsuario, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username

#MODELOS RELACIONADOS A LOS PRODUCTOS
class marca(models.Model):
    idMarca = models.AutoField(primary_key=True)
    nombreMarca = models.CharField(max_length=20, blank=False, null=False)

    def __str__(self):
        return self.nombreMarca
    
class categoriaProducto(models.Model):
    idcategoriaProducto = models.AutoField(primary_key=True)
    nombrecategoriaProducto = models.CharField(max_length=60, blank=False, null=False)

    def __str__(self):
        return self.nombrecategoriaProducto
    
class producto(models.Model):
    idProducto = models.AutoField(primary_key=True)
    nombreProducto = models.TextField(blank=False, null=False)
    precioProducto = models.IntegerField(blank=False, null=False)
    stockProducto = models.IntegerField(blank=False, null=False)
    imagenProducto = models.ImageField(upload_to="productos/", blank=True, null=True)
    descripcionProducto = models.TextField(blank=False, null=False)
    idcategoriaProducto = models.ForeignKey(categoriaProducto, on_delete=models.CASCADE, blank=False, null=False)
    idMarca = models.ForeignKey(marca, on_delete=models.CASCADE, blank=False, null=False)

    def __str__(self):
        return self.nombreProducto
    
    def disminuir_stock(self, cantidad):
        self.stockProducto -= cantidad
        self.save()

#MODELOS RELACIONADOS A LA SUCURSAL
class sucursal(models.Model):
    idSucursal = models.AutoField(primary_key=True)
    nombreSucursal = models.CharField(max_length=50, blank=False, null=False)
    direccionSucursal = models.CharField(max_length=60, blank=False, null=False)
    idComuna = models.ForeignKey(comuna, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombreSucursal

    

#MODELOS RELACIONADOS AL CARRITO DE COMPRA
class Carrito(models.Model):
    usuario = models.OneToOneField(usuarioCustom, on_delete=models.CASCADE)
    productos = models.ManyToManyField(producto, through='ItemCarrito')

    def __str__(self):
        return f"{self.usuario.username}"
    
    
class ItemCarrito(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.producto.nombreProducto} - {self.carrito.usuario.username}"

    def precio_total(self):
        return self.cantidad * self.producto.precioProducto
    
    def calcularDescuentoCarrito(self):
        return round(self.producto.precioProducto - (self.producto.precioProducto * 0.05))
    

class Seguimiento(models.Model):
    descripcion = models.CharField(max_length=250)

    def __str__(self):
        return self.descripcion
    
class Pedido(models.Model):
    carrito = models.ForeignKey(Carrito, on_delete=models.CASCADE)
    numero = models.CharField(max_length=36, unique=True, default=uuid.uuid4)
    fecha = models.DateTimeField(auto_now_add=True)
    estado = models.ForeignKey(Seguimiento, on_delete=models.CASCADE, default=1)
    productos = models.ManyToManyField(producto, through='ItemPedido')
    direccion = models.CharField(max_length=200, blank=True, null=True)
    region = models.ForeignKey(region, on_delete=models.CASCADE, blank=True, null=True)
    comuna = models.ForeignKey(comuna, on_delete=models.CASCADE, blank=True, null=True)
    nombre = models.CharField(max_length=20, blank=True, null=True)
    apellido = models.CharField(max_length=24, blank=True, null=True)
    run = models.CharField(max_length=12, blank=True, null=True)
    correo = models.EmailField(blank=True, null=True)
    sucursal = models.ForeignKey(sucursal, on_delete=models.CASCADE, blank=True, null=True)
    tipo_entrega = models.CharField(max_length=20, choices=[('envio_domicilio', 'Envío a domicilio'), ('retiro_tienda', 'Retiro en tienda')])
    comprobante_pago = models.ImageField(upload_to="comprobantes/", blank=True, null=True)  

    def __str__(self):
        return f"Pedido #{self.numero}"
    
    def calcular_total(self):
        items = self.itempedido_set.all() 
        total = 0

        for item in items:
            total += item.precio_total()
        
        return total
        
    def calcular_cantidad(self):
        items = self.itempedido_set.all()  
        total = 0

        for item in items:
            total += item.cantidad
        
        return total
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
    producto = models.ForeignKey(producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.producto.nombreProducto} - {self.pedido.carrito.usuario.username}"

    def precio_total(self):
        return self.cantidad * self.producto.precioProducto
    


