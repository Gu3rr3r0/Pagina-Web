# Generated by Django 3.2.3 on 2021-07-03 03:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactanos',
            fields=[
                ('idConctactanos', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de contactanos')),
                ('nomCompleto', models.CharField(max_length=50, verbose_name='Nombre completo')),
                ('correoElec', models.CharField(max_length=50, verbose_name='Correo electronico')),
                ('numTelef', models.CharField(max_length=50, verbose_name='Numero de Telefono')),
                ('comentario', models.CharField(max_length=500, verbose_name='Comentario')),
                ('estado', models.CharField(max_length=50, null=True, verbose_name='Estado')),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('idProducto', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del producto')),
                ('tipoProducto', models.CharField(max_length=100, verbose_name='Tipo del Producto')),
                ('nomProducto', models.CharField(max_length=50, verbose_name='Nombre del producto')),
                ('stock', models.IntegerField(verbose_name='Stock del producto')),
                ('descProducto', models.CharField(max_length=200, verbose_name='Descripcion del producto')),
                ('preProducto', models.IntegerField(verbose_name='Precio del producto')),
                ('foto', models.ImageField(null=True, upload_to='productos')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('rutUsuario', models.CharField(max_length=20, primary_key=True, serialize=False, verbose_name='RUT del usuario')),
                ('nomUsuario', models.CharField(max_length=30, verbose_name='Nombre del usuario')),
                ('apellUsuario', models.CharField(max_length=30, verbose_name='Apellido del usuario')),
                ('correo', models.CharField(blank=True, max_length=50, verbose_name='Correo del usuario')),
                ('telefUsuario', models.CharField(blank=True, max_length=15, verbose_name='Telefono usuario')),
                ('direccion', models.CharField(max_length=50, verbose_name='Direccion')),
            ],
        ),
        migrations.CreateModel(
            name='OrdenCompra',
            fields=[
                ('idCompra', models.AutoField(primary_key=True, serialize=False, verbose_name='Id de la compra')),
                ('nomOrden', models.CharField(blank=True, max_length=50, verbose_name='Nombre factura')),
                ('cantComprado', models.IntegerField(verbose_name='Cantidad del producto comprado')),
                ('tipoRetiro', models.CharField(max_length=50, verbose_name='Tipo Retiro del producto')),
                ('tipoPago', models.CharField(max_length=30, verbose_name='Tipo de pago del producto')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginaweb.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginaweb.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Carrito',
            fields=[
                ('idCarrito', models.AutoField(primary_key=True, serialize=False, verbose_name='Id del carrito')),
                ('cantidadProd', models.IntegerField(verbose_name='Cantidad de Producto')),
                ('totalProd', models.IntegerField(verbose_name='Total a Pagar')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginaweb.producto')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='paginaweb.usuario')),
            ],
        ),
    ]