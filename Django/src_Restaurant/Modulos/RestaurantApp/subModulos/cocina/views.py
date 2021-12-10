from django.http.response import HttpResponse
from django.shortcuts import render,redirect, resolve_url
from Modulos.LoginApp.views import ComprobarUsuario
from Modulos.RestaurantApp.subModulos.cocina.carrito import Carrito
from Modulos.RestaurantApp.subModulos.cocina.forms import formularioMenu
from Modulos.RestaurantApp import models


def index(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"COCINA")
    if(logeado and rolCorrecto):
        return render(request, "cocina/indexCocina.html")
    else:
        return redirect(linkredireccion)

#---------------------------------------TableroCocina---------------------------------- ConfirmarOrdenHtmx
def tablero(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"COCINA")
    if(logeado and rolCorrecto):
        data = {'Lista':models.listarOrdenesClienteTablero()}
        return render(request, "cocina/tablero.html",data)
    else:
        return redirect(linkredireccion)
def CargarRecetasTableroHtmx(request):
    id = request.GET.get('id')
    data = {'ListaTableroDetalles':models.listarDetallesOrdenesClienteTablero(id)}
    return render(request, "cocina/tableroDetalles.html",data)

def ConfirmarOrdenClienteHtmx(request):
    try:
        print("ConfirmarOrdenHtmxConfirmarOrdenHtmxConfirmarOrdenHtmxConfirmarOrdenHtmx")
        id = request.GET.get('id')
        resultado = models.ConfirmarOrdenCliente(id)
        listaResultados = models.listarOrdenesClienteTablero()
        data = {'listaResultados':listaResultados,'resultado': resultado}
        return render(request, "cocina/tableroOrdenLista.html",data)
    except Exception as e:
        print(e)
        listaResultados = models.listarOrdenesProducto()
        data = {'listaResultados':listaResultados,'resultado': 0}
        return render(request, "cocina/tableroOrdenLista.html",data)  

#---------------------------------------Recetas----------------------------------
#--------------------------Modulo de creacion de Recetas-------------------------
def receta(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"COCINA")
    if(logeado and rolCorrecto):
        data = {'Lista':models.listarProductos(),'totalCarrito':total_carrito(request)}
        return render(request, "cocina/receta.html",data)
    else:
        return redirect(linkredireccion)
    
def AgregarProductosRecetaHtmx(request):
    id = request.GET.get('id')
    carrito = Carrito(request)
    producto = models.Product.objects.get(productid=id)
    carrito.agregar(producto)
    data = {'totalCarrito':total_carrito(request)}
    return render(request, "cocina/tablaRecetaHtmx.html",data)

def EliminarProductosRecetaHtmx(request):
    id = request.GET.get('id')
    carrito = Carrito(request)
    producto = models.Product.objects.get(productid=id)
    carrito.eliminar(producto)
    data = {'totalCarrito':total_carrito(request)}
    return render(request, "cocina/tablaRecetaHtmx.html",data)

def RestarProductosRecetaHtmx(request):
    id = request.GET.get('id')
    carrito = Carrito(request)
    producto = models.Product.objects.get(productid=id)
    carrito.restar(producto)
    data = {'totalCarrito':total_carrito(request)}
    return render(request,"cocina/tablaRecetaHtmx.html",data)

def LimpiarProductosRecetaHtmx(request):
    carrito = Carrito(request)
    carrito.limpiar()
    data = {'totalCarrito':0}
    return render(request, "cocina/LimpiarProductosRecetaHtmx.html",data)


def total_carrito(request):
    total = 0
    if "carritoReceta" in request.session.keys():
        for key, value in request.session["carritoReceta"].items():            
            total += int(value["acumulado"])
    return total

def ModalGuardarDatosProductosRecetanHtmx(request):
    data = {'form': formularioMenu()}
    return render(request, "cocina/modalGuardarMenuHtmx.html",data)

def GuardarDatosProductosRecetaHtmx(request):
    try:
        totalCarrito= total_carrito(request)
        resultado = -1
        #Genera Menu        
        if request.method=="POST":
            #Obtiene los datos del formulario
            formulario=formularioMenu(request.POST)
            #Comprueba si el formulario es Valido y si existe carrito
            carrito = request.session.get("carritoReceta").items()
            if formulario.is_valid() and carrito:
                #Obtiene La Info del formulario
                infForm = formulario.cleaned_data
                resultado,idMenu = models.AgregarMenuProducto(infForm['name'],infForm['recipe'],infForm['cookingtime'],totalCarrito,infForm['menuprice'])
                if resultado == 1:
                    #Crea Lista CarritoMenu
                    listCarritoMenu = []
                    carrito = request.session.get("carritoReceta").items()
                    for key, value in carrito:
                        carrito = models.Menu.products.through(pmproductid = models.Product.objects.get(productid=value["producto_id"]), pmmenuid= models.Menu.objects.get(menuid=idMenu),quantity=value["cantidad"],total=value["acumulado"])
                        listCarritoMenu.append(carrito)
                    models.Menu.products.through.objects.bulk_create(listCarritoMenu)
                    carrito = Carrito(request)
                    carrito.limpiar()
                    data = {'resultado': resultado}
                    return render(request, "cocina/guardarProductosOrdenHtmx.html",data)
                elif resultado == -1:
                    data = {'resultado': resultado}
                    return render(request, "cocina/guardarProductosOrdenHtmx.html",data)
        data = {'totalCarrito':totalCarrito,'resultado': 0}
        return render(request, "cocina/guardarProductosOrdenHtmx.html",data)
    except Exception as e:
        print("Error")
        print (e)
        #models.EliminarOrdenProducto(idOrden)
        data = {'totalCarrito':totalCarrito,'resultado': 0}
        return render(request, "cocina/guardarProductosOrdenHtmx.html",data)

#---------Modulo lista,edicion,eliminacion Receta-----------

def recetas(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"COCINA")
    if(logeado and rolCorrecto):

        data = {'Lista':models.listarMenusProducto()}

        return render(request, "cocina/recetas.html",data)
    else:
        return redirect(linkredireccion)

def DetallesRecetasProductoHtmx(request):
        id = request.GET.get('id')
        receta = request.GET.get('receta')
        data = {'ListaMenus':models.listarMenusProductoDetalles(id),'receta':receta}
        return render(request, "cocina/recetasProductoDetalles.html",data)
  
def EliminarRecetasProductoHtmx(request):
    try:
        id = request.GET.get('id')
        resultado = models.EliminarMenuProducto(id) 
        listaResultados = models.listarMenusProducto()
        data = {'Lista':listaResultados,'resultado': resultado}
        return render(request, "cocina/eliminarRecetaProductoHtmx.html",data)
    except:
        data = {'Lista':listaResultados,'resultado': 0}
        return render(request, "cocina/eliminarRecetaProductoHtmx.html",data)     
#Modal Eliminar receta
def ModalEliminarRecetaProductoHtmx(request):
    id = request.GET.get('id')
    data = {'resultadoid':id} 
    return render(request, "cocina/modalEliminarRecetaProducto.html",data)