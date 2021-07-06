from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField



class Usuario(models.Model):
    rutUsuario = models.CharField(primary_key=True, max_length=20, verbose_name='RUT del usuario')
    nomUsuario = models.CharField(max_length=30, verbose_name='Nombre del usuario', blank=False)
    apellUsuario = models.CharField(max_length=30, verbose_name='Apellido del usuario', blank=False)
    correo = models.CharField(max_length=50, verbose_name='Correo del usuario', blank=True)
    telefUsuario = models.CharField(max_length=15, verbose_name='Telefono usuario',blank=True)
    direccion = models.CharField(max_length=50, verbose_name='Direccion', blank=False)

    def __str__(self):
        return self.nomUsuario



class Producto(models.Model):
    idProducto = models.AutoField(primary_key=True, verbose_name='Id del producto')
    tipoProducto = models.CharField(max_length=100, verbose_name='Tipo del Producto', blank=False)
    nomProducto = models.CharField(max_length=50, verbose_name='Nombre del producto', blank=False)
    stock = models.IntegerField(verbose_name='Stock del producto', blank=False)
    descProducto = models.CharField(max_length=200, verbose_name='Descripcion del producto', blank=False)
    preProducto = models.IntegerField(verbose_name='Precio del producto', blank=False)
    foto = models.ImageField(upload_to="productos", null= True)


    def __str__(self):
        return self.nomProducto

class OrdenCompra(models.Model):
    idCompra = models.AutoField(primary_key=True, verbose_name='Id de la compra')
    nomOrden = models.CharField(max_length=50, verbose_name='Nombre factura', blank=True)
    cantComprado = models.IntegerField(verbose_name= 'Cantidad del producto comprado', blank=False)
    tipoRetiro = models.CharField(max_length=50, verbose_name='Tipo Retiro del producto', blank=False)
    tipoPago = models.CharField(max_length=30, verbose_name='Tipo de pago del producto', blank=False)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
    

    def __str__(self):
        return self.nomOrden

class Contactanos(models.Model):
    idConctactanos = models.AutoField(primary_key=True, verbose_name='Id de contactanos')
    nomCompleto = models.CharField(max_length=50, verbose_name='Nombre completo', blank=False)
    correoElec = models.CharField(max_length=50, verbose_name= 'Correo electronico', blank=False)
    numTelef = models.CharField(max_length=50, verbose_name='Numero de Telefono', blank=False)
    comentario = models.CharField(max_length=500, verbose_name='Comentario', blank=False)
    estado = models.CharField(max_length=50, verbose_name='Estado', blank=False, null=True)
    

    def __str__(self):
        return self.nomCompleto

class Carrito(models.Model):
    idCarrito = models.AutoField(primary_key=True, verbose_name='Id del carrito')
    cantidadProd = models.IntegerField(verbose_name='Cantidad de Producto', blank=False, null=False)
    totalProd = models.IntegerField(verbose_name='Total a Pagar', blank=False, null=False)
    producto = models.ForeignKey(Producto,on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario,on_delete=models.CASCADE)
