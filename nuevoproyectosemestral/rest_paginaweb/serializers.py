from django.db.models.base import Model
from paginaweb.models import Producto
from rest_framework import serializers

class ProductoSerializador(serializers.ModelSerializer):
    class Meta:
            model = Producto
            fields = ['idProducto','tipoProducto','nomProducto','stock','descProducto','preProducto','foto']