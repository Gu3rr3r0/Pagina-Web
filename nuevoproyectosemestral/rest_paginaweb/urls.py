from django.urls import path
from rest_paginaweb.views import vista_producto, datos_producto
from rest_paginaweb.viewslogin import login


urlpatterns = [
    path('lista_producto',vista_producto, name="lista_producto"),
    path('datos_producto/<id>',datos_producto, name="datos_producto"),
    path('login',login,name="login"),
]