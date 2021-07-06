from django.db.models.query import QuerySet
from django.core.exceptions import RequestAborted
from django.db.models.fields import PositiveBigIntegerField
from django.shortcuts import render, redirect
from django.urls.conf import path
from .models import Usuario, Producto, Contactanos, Carrito
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Sum

# Create your views here.
def home(request):

    return render(request,'paginaweb/home.html')

def buscar(request):
    querySet = request.GET.get("buscar")
         
    if querySet:
        producto = Producto.objects.filter(
            Q(nomProducto__icontains = querySet)
        ).distinct()
        contexto = {"producto":producto}
    else:
        producto = Producto.objects.all()
        contexto = {"producto":producto}
       
    return render(request,'paginaweb/buscar.html', contexto)

def celulares(request):
    querySet = 'Celular'
         
    if querySet:
        celulares = Producto.objects.filter(
            Q(tipoProducto__icontains = querySet)
        ).distinct()
        contexto = {"celulares":celulares}
    else:
        celulares = Producto.objects.all()
        contexto = {"celulares":celulares}

    return render(request,'paginaweb/celulares.html', contexto)

def contactanos(request):
    contactanos = Contactanos.objects.all()
    contexto = {"contactanos":contactanos}
    return render(request,'paginaweb/contactanos.html', contexto)

def crearcuenta(request): 
    return render(request,'paginaweb/crearcuenta.html')

def registrarusuario(request):
    rutUsuario_u = request.POST['rutu']
    nomUsuario_u  = request.POST['nombreu']
    conUsuario_u  = request.POST['contrau']
    apellUsuario_u  = request.POST['apellidou']
    correo_u  = request.POST['emailu']
    telefUsuario_u  = request.POST['numerou']
    direccion_u  = request.POST['direccionu']

    User.objects.create_user(id= int(rutUsuario_u), password = conUsuario_u,is_superuser=0,username = correo_u, first_name = nomUsuario_u, last_name = apellUsuario_u, email = correo_u, is_staff=0, is_active=1)
    Usuario.objects.create(rutUsuario = rutUsuario_u, nomUsuario = nomUsuario_u, apellUsuario = apellUsuario_u, correo = correo_u, telefUsuario = telefUsuario_u, direccion = direccion_u)

    messages.success(request,'La cuenta ha sido creada correctamente')
    return redirect('acceso')
    

def listadosolicitud(request):
    listado = Contactanos.objects.all()
    contexto = {"listado":listado}

    return render(request,'paginaweb/listadosolicitud.html', contexto)

def nosotros(request):

    return render(request,'paginaweb/nosotros.html')

def notebooks(request):
    querySet = 'Notebook'
         
    if querySet:
        notebook = Producto.objects.filter(
            Q(tipoProducto__icontains = querySet)
        ).distinct()
        contexto = {"notebook":notebook}
    else:
        notebook = Producto.objects.all()
        contexto = {"notebook":notebook}
 
    return render(request,'paginaweb/notebooks.html', contexto)


def recuperar(request):

    return render(request,'paginaweb/recuperar.html')

def sucursales(request):

    return render(request,'paginaweb/sucursales.html')

def televisores(request):
    querySet = 'Televisor'
         
    if querySet:
        televisor = Producto.objects.filter(
            Q(tipoProducto__icontains = querySet)
        ).distinct()
        contexto = {"televisor":televisor}
    else:
        televisor = Producto.objects.all()
        contexto = {"televisor":televisor}

    return render(request,'paginaweb/televisores.html', contexto)

def formulario_contacto(request):
    nombre_f = request.POST['nombre_completo']
    correo_f = request.POST['correo']
    numero_f = request.POST['telefono']
    comentario_f = request.POST['comentario']
    estado_f = 'Pendiente'

    Contactanos.objects.create(nomCompleto = nombre_f, correoElec = correo_f, numTelef = numero_f, comentario = comentario_f, estado = estado_f)

    messages.success(request,'Su formulario ha sido enviado correctamente')

    return redirect(contactanos)

def eliminar_solicitud(request, id):
    eliminar = Contactanos.objects.get(idConctactanos = id)
    eliminar.delete()
    messages.success(request, 'Solicitud eliminada')

    return redirect('listadosolicitud')

def modificar_solicitud(request, id):
    modificar = Contactanos.objects.get(idConctactanos  = id)
    
    contexto = { "modificar" : modificar }

    return render(request, 'paginaweb/modificarsolicitud.html', contexto)

def remplazar(reques):
    idConctactanos_r = reques.POST['numero_solicitud']
    nomCompleto_r = reques.POST['nombre_completo']
    correoElec_r = reques.POST['correo']
    numTelef_r = reques.POST['telefono']
    comentario_r = reques.POST['comentario']
    estado_r = reques.POST['estado']

    contactanos = Contactanos.objects.get(idConctactanos = idConctactanos_r)
    contactanos.nomCompleto = nomCompleto_r
    contactanos.correoElec = correoElec_r
    contactanos.numTelef = numTelef_r
    contactanos.comentario = comentario_r
    contactanos.estado = estado_r
    contactanos.save()

    messages.success(reques,'Se ha actualizado la solicitud')
    return redirect('listadosolicitud')

def listadoproductos(request):
    listadop = Producto.objects.all()
    contexto = {"listadop":listadop}

    return render(request,'paginaweb/listadoproductos.html', contexto)

def registrarproducto(request):
    contactanos = Contactanos.objects.all()
    contexto = {"contactanos":contactanos}
    return render(request,'paginaweb/registrarproducto.html', contexto)

def registroproducto(request):
    tipoProducto_p = request.POST['tipoproducto']
    nomProducto_p = request.POST['marca']
    stock_p = request.POST['stockp']
    descProducto_p = request.POST['descriproducto']
    preProducto_p = request.POST['precio']
    foto_p = request.FILES['foto_p']

    Producto.objects.create(tipoProducto = tipoProducto_p, nomProducto = nomProducto_p, stock = stock_p, descProducto = descProducto_p, preProducto = preProducto_p, foto= foto_p)

    messages.success(request,'El producto ha sido registrado correctamente')

    return render(request,'paginaweb/registrarproducto.html')

def eliminar_producto(request, id):
    eliminarp = Producto.objects.get(idProducto = id)
    eliminarp.delete()
    messages.success(request, 'Producto eliminado')

    return redirect('listadoproductos')


def modificar_producto(request, id):
    modificarp = Producto.objects.get(idProducto  = id)
    
    contexto = { "modificarp" : modificarp }

    return render(request, 'paginaweb/modificarproducto.html', contexto)

def remplazarproducto(reques):
    idProducto_rp = reques.POST['codigoproducto']
    tipoProducto_rp = reques.POST['tipoproduc']
    nomProducto_rp = reques.POST['marcap']
    stock_rp = reques.POST['stockpp']
    descProducto_rp = reques.POST['descriproduc']
    preProducto_rp = reques.POST['preciop']
    foto_rp = reques.FILES['foto_mp']

    producto = Producto.objects.get(idProducto = idProducto_rp)
    producto.tipoProducto = tipoProducto_rp
    producto.nomProducto = nomProducto_rp
    producto.stock = stock_rp
    producto.descProducto = descProducto_rp
    producto.preProducto = preProducto_rp
    print (foto_rp)
    if foto_rp is None:
        producto.foto = 'productos/3.png'
        
        
    else:
        producto.foto = foto_rp
    producto.save()

    messages.success(reques,'Se ha actualizado el producto')
    return redirect('listadoproductos')

def login_view(request):

    u = request.POST['username']

    c = request.POST['password']

    user = authenticate(username = u, password = c)

    if user is not None:

        if user.is_active:

            login(request,user)
            return redirect('home')

        else:

            messages.error(request,'Usuario Inactivo')
    else:

        messages.error(request,'Usuario y/o contraseña incorrecta')

        return redirect('acceso')

def logout_view(request):

    logout(request)

    return redirect('home')

def ver_carrito(request):
    user = Usuario.objects.get(rutUsuario = request.user.id)
    listadoc = Carrito.objects.filter(usuario = user).order_by('idCarrito')

    suma2 = Carrito.objects.filter(usuario = user).count()

    if suma2 == 0:
        suma = 0
        x = 0
    else:
        suma = Carrito.objects.filter(usuario = user).aggregate(Sum('totalProd'))
        x = 1
    contexto = {
        "listadoc":listadoc,
        "suma":suma,
        "x":x,
    }

    return render(request,'paginaweb/carrito.html', contexto)

def carrito_celular(request, id):
    cant = 1
    celular = Producto.objects.get(idProducto = id)
    usuario = Usuario.objects.get(rutUsuario = request.user.id)
    total = int(cant) * int(celular.preProducto)
    
    Carrito.objects.create(producto = celular,cantidadProd = cant , totalProd= total,usuario = usuario)
    messages.success(request,'El Celular a sido agregado al carrito correctamente.')
    return redirect('celulares')

def carrito_notebook(request, id):
    cant = 1
    notebook = Producto.objects.get(idProducto = id)
    usuario = Usuario.objects.get(rutUsuario = request.user.id)
    total = int(cant) * int(notebook.preProducto)
    
    Carrito.objects.create(producto = notebook,cantidadProd = cant , totalProd= total,usuario = usuario)
    messages.success(request,'El Notebook a sido agregado al carrito correctamente.')
    return redirect('notebooks')

def carrito_televisor(request, id):
    cant = 1
    televisor = Producto.objects.get(idProducto = id)
    usuario = Usuario.objects.get(rutUsuario = request.user.id)
    total = int(cant) * int(televisor.preProducto)
    
    Carrito.objects.create(producto = televisor,cantidadProd = cant , totalProd= total,usuario = usuario)
    messages.success(request,'El Televisor a sido agregado al carrito correctamente.')
    return redirect('televisores')

def eliminar_carrito(request, id):
    carrito = Carrito.objects.get(idCarrito = id)
    carrito.delete()
    messages.success(request,'El producto a sido eliminado del carrito.')
    return redirect('carritocompra')

def pagar(request):
    user1 = Usuario.objects.get(rutUsuario = request.user.id)
    carrito = Carrito.objects.filter(usuario = user1)

    for c in carrito:
        prod = Producto.objects.get(idProducto = c.producto.idProducto)
        prod.stock = prod.stock - c.cantidadProd
        prod.save()

    carrito.delete()
    messages.success(request,'!Gracias por su compra!')
    messages.success(request,'(Se ha vaciado el carrito)')
    return redirect('carritocompra')