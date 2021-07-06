from paginaweb.views import contactanos
from django.contrib import admin
from .models import Carrito, Usuario, Producto, OrdenCompra, Contactanos
# Register your models here.

admin.site.register(Usuario)
admin.site.register(Producto)
admin.site.register(OrdenCompra)
admin.site.register(Contactanos)
admin.site.register(Carrito)