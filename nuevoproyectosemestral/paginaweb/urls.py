from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.decorators import login_required
from .views import  home, buscar, celulares, contactanos, crearcuenta, login_view , logout_view ,nosotros,\
   notebooks, recuperar, remplazar, sucursales, televisores, formulario_contacto, listadosolicitud, eliminar_solicitud, \
   modificar_solicitud, remplazar, listadoproductos, registrarproducto, registroproducto, eliminar_producto, modificar_producto,\
  remplazarproducto, registrarusuario, ver_carrito, eliminar_carrito, carrito_celular,carrito_notebook,carrito_televisor, pagar

urlpatterns = [
  path('', home, name="home"),
  path('buscar', buscar, name="buscar"),
  path('celulares', celulares, name="celulares"),
  path('contactanos', contactanos, name="contactanos"),
  path('crearcuenta', crearcuenta, name="crearcuenta"),
  path('nosotros', nosotros, name="nosotros"),
  path('notebooks', notebooks, name="notebooks"),
  path('recuperar', recuperar, name="recuperar"),
  path('sucursales', sucursales, name="sucursales"),
  path('televisores', televisores, name="televisores"),
  path('formulario_contacto', formulario_contacto, name="formulario_contacto"),
  path('listadosolicitud', login_required(listadosolicitud), name="listadosolicitud"),
  path('eliminar/<int:id>',login_required(eliminar_solicitud), name='eliminar_solicitud'),
  path('modificar/<int:id>)',login_required(modificar_solicitud), name='modificar_solicitud'),
  path('remplazar', remplazar, name="remplazar"),
  path('registrarproducto', login_required(registrarproducto), name="registrarproducto"),
  path('listadoproductos', login_required(listadoproductos), name="listadoproductos"),
  path('registroproducto', registroproducto, name="registroproducto"),
  path('eliminarp/<int:id>',login_required(eliminar_producto), name='eliminar_producto'),
  path('modificarp/<int:id>)',login_required(modificar_producto), name='modificar_producto'),
  path('remplazarproducto', remplazarproducto, name="remplazarproducto"),
  path('registrarusuario', registrarusuario, name="registrarusuario"),
  path('carritocompra', login_required(ver_carrito), name="carritocompra"),
  path('carrito_celular/<int:id>', login_required(carrito_celular), name="carrito_celular"),
  path('carrito_notebook/<int:id>', login_required(carrito_notebook), name="carrito_notebook"),
  path('carrito_televisor/<int:id>', login_required(carrito_televisor), name="carrito_televisor"),
  path('eliminar_carrito/<int:id>',login_required(eliminar_carrito), name='eliminar_carrito'),
  path('pagar',login_required(pagar), name='pagar'),


  path('acceso/',LoginView.as_view(template_name='paginaweb/iniciosesion.html'),name="acceso"),
  path('sesion',login_view,name="sesion"),
  path('logout',logout_view,name="logout"),
]
