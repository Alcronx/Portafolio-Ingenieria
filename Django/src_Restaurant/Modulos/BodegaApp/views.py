from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from Modulos.BodegaApp.Carrito import Carrito
from Modulos.LoginApp.views import ComprobarUsuario
from Modulos.BodegaApp import models
from Modulos.BodegaApp.forms import formularioStockProducto
from Restaurant.settings import MESSAGE_STORAGE

# Create your views here.

def index(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"BODEGA")
    if(logeado and rolCorrecto):
        
        
        
        return render(request, "indexBodega.html")
    else:
        return redirect(linkredireccion)
      
#----------------------------Ordenes--------------------------------
#----------Modulo Creacion Orden------------------------------------
def orden(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"BODEGA")
    if(logeado and rolCorrecto):
        data = {'cbxProveedor':models.ListarProveedorescbx(),'totalCarrito':0}
        return render(request, "Orden/orden.html",data)
    else:
        return redirect(linkredireccion)
    
def ListarProductosOrdenHtmx(request):
    id =  request.POST.get("cbxProductos","1")
    carrito = Carrito(request)
    carrito.limpiar()
    data = {'ListaProductos':models.ProductosProveedores(id)} 
    return render(request, "Orden/listarProductosOrdenHtmx.html",data)

def AgregarProductosOrdenHtmx(request):
    id = request.GET.get('id')
    carrito = Carrito(request)
    producto = models.Product.objects.get(productid=id)
    carrito.agregar(producto)
    data = {'totalCarrito':total_carrito(request)}
    return render(request, "Orden/tablaOrdenHtmx.html",data)

def EliminarProductosOrdenHtmx(request):
    id = request.GET.get('id')
    carrito = Carrito(request)
    producto = models.Product.objects.get(productid=id)
    carrito.eliminar(producto)
    data = {'totalCarrito':total_carrito(request)}
    return render(request, "Orden/tablaOrdenHtmx.html",data)

def RestarProductosOrdenHtmx(request):
    id = request.GET.get('id')
    carrito = Carrito(request)
    producto = models.Product.objects.get(productid=id)
    carrito.restar(producto)
    data = {'totalCarrito':total_carrito(request)}
    return render(request,"Orden/tablaOrdenHtmx.html",data)

def LimpiarProductosOrdenHtmx(request):
    carrito = Carrito(request)
    carrito.limpiar()
    data = {'totalCarrito':0}
    return render(request, "Orden/LimpiarProductosOrdenHtmx.html",data)

def GuardarDatosProductosOrdenHtmx(request):
    try:
        totalCarrito= total_carrito(request)
        #Genera Orden
        resultadoAOP,idOrden = models.AgregarOrdenProducto(totalCarrito)
        if resultadoAOP == 1:
            #Crea Lista Carrito
            listCarrito = []
            carrito = request.session.get("carrito").items()
            for key, value in carrito:
                carrito = models.Orderproduct.products.through(opdproductid = models.Product.objects.get(productid=value["producto_id"]), opdorderproductid= models.Orderproduct.objects.get(orderproductid=idOrden),quantity=value["cantidad"],total=value["acumulado"])
                listCarrito.append(carrito)
            models.Orderproduct.products.through.objects.bulk_create(listCarrito)
            carrito = Carrito(request)
            carrito.limpiar()
        data = {'totalCarrito':totalCarrito,'resultado': 1}
        return render(request, "Orden/guardarProductosOrdenHtmx.html",data)
    except:
        models.EliminarOrdenProducto(idOrden)
        data = {'totalCarrito':totalCarrito,'resultado': 0}
        return render(request, "Orden/guardarProductosOrdenHtmx.html",data)

def total_carrito(request):
    total = 0
    if "carrito" in request.session.keys():
        for key, value in request.session["carrito"].items():
            total += int(value["acumulado"])
    return total
#---------Modulo lista,edicion,eliminacion orden-----------

def ordenes(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"BODEGA")
    if(logeado and rolCorrecto):

        data = {'Lista':models.listarOrdenesProducto()}

        return render(request, "Orden/ordenes.html",data)
    else:
        return redirect(linkredireccion)

def DetallesOrdenesProductoHtmx(request):
        id = request.GET.get('id')
        data = {'ListaOrdenes':models.listarOrdenesProductoDetalles(id)}
        return render(request, "Orden/ordenesProductoDetalles.html",data)
  

def ConfirmarOrdenesProductoHtmx(request):
    try:
        id = request.GET.get('id')
        resultado = models.ConfirmarOrdenProducto(id)
        listaResultados = models.listarOrdenesProducto()
        data = {'Lista':listaResultados,'resultado': resultado}
        return render(request, "Orden/confirmarOrdenProductoHtmx.html",data)
    except Exception as e:
        print(e)
        listaResultados = models.listarOrdenesProducto()
        data = {'Lista':listaResultados,'resultado': 0}
        return render(request, "Orden/confirmarOrdenProductoHtmx.html",data)  

def DesconfirmarOrdenesProductoHtmx(request):
    try:
        id = request.GET.get('id')
        resultado = models.DesconfirmarOrdenProducto(id)
        listaResultados = models.listarOrdenesProducto()
        data = {'Lista':listaResultados,'resultado': resultado}
        return render(request, "Orden/DesconfirmarOrdenProductoHtmx.html",data)
    except Exception as e:
        print(e)
        listaResultados = models.listarOrdenesProducto()
        data = {'Lista':listaResultados,'resultado': 0}
        return render(request, "Orden/DesconfirmarOrdenProductoHtmx.html",data)  

def EliminarOrdenesProductoHtmx(request):
    try:
        id = request.GET.get('id')
        resultado = models.EliminarOrdenProducto(id) 
        listaResultados = models.listarOrdenesProducto()
        data = {'Lista':listaResultados,'resultado': resultado}
        return render(request, "Orden/eliminarOrdenProductoHtmx.html",data)
    except:
        data = {'Lista':listaResultados,'resultado': 0}
        return render(request, "Orden/eliminarOrdenProductoHtmx.html",data)     
#Modal Eliminar proveedor
def ModalEliminarOrdenProductoHtmx(request):
    id = request.GET.get('id')
    data = {'resultadoid':id} 
    return render(request, "Orden/modalEliminarOrdenProducto.html",data)
#----------------------------Fin Ordenes--------------------------------
#---------------------------------------------------  vista Stock Producto ---------------------------------------------------------
#Funcion que muestra la pagina para administras Stock
def stockproducto(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"BODEGA")
    if(logeado and rolCorrecto):
        data = {'Lista':models.listarStocksProducto()}
        return render(request, "Stock/stockproducto.html",data)
    else:
        return redirect(linkredireccion)
#Funcion que muestra Stock Producto
def DetallesStockProductoHtmx(request):
    id = request.GET.get('id')
    detalles = models.DetallesStocksProductos(id)
    for lista in detalles:
        productname = lista[4]
        stock = lista[2]
        criticalstock = lista[3]
    DatosFormulario = {
        "stock" : stock,
        "criticalstock" : criticalstock,
    }
    formularioEditar = formularioStockProducto(initial=DatosFormulario)
    data = {'FormularioEditar':formularioEditar,'resultadoid':id,'NombreProducto': productname}
    return render(request, "Stock/detallesStockProducto.html",data)
#Funcion para editar Stock Producto
def EditarStockProductoHtmx(request):
    id = request.GET.get('id')
    resultado = -1
    if request.method=="POST":
        #Obtiene los datos del formulario
        formulario=formularioStockProducto(request.POST)
        #Comprueba si el formulario es Valido
        if formulario.is_valid():
            #Obtiene La Info del formulario
            infForm = formulario.cleaned_data  
            resultado = models.EditarStocksProductos(infForm['stock'],infForm['criticalstock'],id)  
            listaResultados = models.listarStocksProducto()
            if resultado == 1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Stock/editarStockProducto.html",data)
            elif resultado == -1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Producto/editarStockProducto.html",data)
    listaResultados = models.listarStocksProducto()
    data = {'Lista':listaResultados,'resultado': 0}
    return render(request, "Producto/editarStockProducto.html",data)
#---------------------------------------------------  Fin Stock Producto ---------------------------------------------------




 







