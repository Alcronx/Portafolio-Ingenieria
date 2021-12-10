from django.forms.fields import DateField
from django.shortcuts import redirect, render
from Modulos.AdminApp import models
from Modulos.LoginApp.models import Login 
from Modulos.LoginApp.views import ComprobarUsuario
from Modulos.AdminApp.forms import formularioMesero, formularioUsuario,formularioMesa,formularioReserva,formularioProveedor,formularioProducto
# Create your views here.

def index(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"ADMIN")
    if(logeado and rolCorrecto):       
        return render(request, "indexAdmin.html")
    else:
        return redirect(linkredireccion)



def reporte(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"ADMIN")
    if(logeado and rolCorrecto):
        data = {'Lista':models.mostrarMenusVendidosDia(),'Lista1':models.mostrarProductosOrdenadosDia(),'Lista2':models.mostrarGananciaMenuDia()}
        return render(request, "Reporte/reporte.html",data)
    else:
        return redirect(linkredireccion)
    
#---------------------------------------------------  vista Mesas ---------------------------------------------------
#Funcion que muestra la pagina para administras Mesas
def mesa(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"ADMIN")
    if(logeado and rolCorrecto):
        data = {'Lista':models.listarMesas(),'form': formularioMesa()}
        return render(request, "Mesa/mesa.html",data)
    else:
        return redirect(linkredireccion)
#Funcion que Agrega Mesa y muestra tabla
def AgregarMesaHtmx(request):
    resultado = -1
    if request.method=="POST":
        #Obtiene los datos del formulario
        formulario=formularioMesa(request.POST)
        #Comprueba si el formulario es Valido
        if formulario.is_valid():
            #Obtiene La Info del formulario
            infForm = formulario.cleaned_data  
            resultado = models.AgregarMesas(infForm['tableNumber'],infForm['tableMembers'],infForm['aviable'])            
            listaResultados = models.listarMesas()
            if resultado == 1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Mesa/agregarMesa.html",data)
            elif resultado == -1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Mesa/agregarMesa.html",data)
    listaResultados = models.listarMesas()
    data = {'Lista':listaResultados,'resultado': 0}
    return render(request, "Mesa/agregarMesa.html",data)
#Funcion que muestra 1 Mesa
def DetallesMesaHtmx(request):
    id = request.GET.get('id')
    detalles = models.DetallesMesas(id)
    for lista in detalles:
        tableNumber = lista[1]
        tableMembers = lista[2]
        aviable = lista[3]
    DatosFormulario = {
        "tableNumber" : tableNumber,
        "tableMembers" : tableMembers,
        "aviable":aviable,
    }
    formularioEditar = formularioMesa(initial=DatosFormulario)
    data = {'FormularioEditar':formularioEditar,'resultadoid':id}
    return render(request, "Mesa/detallesMesa.html",data)
#Funcion para editar un Mesa
def EditarMesaHtmx(request):
    id = request.GET.get('id')
    resultado = -1
    if request.method=="POST":
        #Obtiene los datos del formulario
        formulario=formularioMesa(request.POST)
        #Comprueba si el formulario es Valido
        if formulario.is_valid():
            #Obtiene La Info del formulario
            infForm = formulario.cleaned_data  
            resultado = models.EditarMesas(infForm['tableNumber'],infForm['tableMembers'],infForm['aviable'],id) 
            listaResultados = models.listarMesas()
            if resultado == 1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Mesa/editarMesa.html",data)
            elif resultado == -1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Mesa/editarMesa.html",data) 
    Usuarios = models.listarUsuarios()
    data = {'Lista':Usuarios,'resultado': 0}
    return render(request, "Mesa/editarMesa.html",data)
#Funcion para Eliminar Mesa
def EliminarMesaHtmx(request):
    try:
        id = request.GET.get('id')
        resultado = models.EliminarMesas(id) 
        listaResultados = models.listarMesas()
        data = {'Lista':listaResultados,'resultado': resultado}
        return render(request, "Mesa/eliminarMesa.html",data)
    except:
        data = {'Lista':listaResultados,'resultado': 0}
        return render(request, "Mesa/eliminarMesa.html",data)      
#Modal Eliminar Mesa
def ModalEliminarMesaHtmx(request):
    id = request.GET.get('id')
    data = {'resultadoid':id} 
    return render(request, "Mesa/modalEliminarMesa.html",data)
#---------------------------------------------------  Fin vista Mesas ---------------------------------------------------

#---------------------------------------------------  vista Usuarios ---------------------------------------------------
# Funcion que muestra la pagina para administras Usuarios
def usuario(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"ADMIN")
    if(logeado and rolCorrecto):
        data = {'ListaUsuarios':models.listarUsuarios(),'formLogin': formularioUsuario()}
        return render(request, "Usuario/usuario.html",data)
    else:
        return redirect(linkredireccion)
#Funcion que Agrega Usuario y muestra tabla
def AgregarUsuarioHtmx(request):
    resultado = -1
    if request.method=="POST":
        #Obtiene los datos del formulario
        formulario=formularioUsuario(request.POST)
        #Comprueba si el formulario es Valido
        if formulario.is_valid():
            #Obtiene La Info del formulario
            infForm = formulario.cleaned_data
            resultadoConsulta = Login.objects.filter(username=infForm['username'],passworduser=infForm['passworduser']).exists()
            if not(resultadoConsulta):
                resultado = models.AgregarUsuarios(infForm['username'],infForm['passworduser'],infForm['rol'])
            else:
                resultado = -1           
            Usuarios = models.listarUsuarios()
            if resultado == 1:
                data = {'ListaUsuarios':Usuarios,'resultado': resultado}
                return render(request, "Usuario/agregarUsuario.html",data)
            elif resultado == -1:
                data = {'ListaUsuarios':Usuarios,'resultado': resultado}
                return render(request, "Usuario/agregarUsuario.html",data) 
    Usuarios = models.listarUsuarios()
    data = {'ListaUsuarios':Usuarios,'resultado': resultado}
    return render(request, "Usuario/agregarUsuario.html",data)
#Funcion para editar un Usuario
def EditarUsuarioHtmx(request):
    idUsuario = request.GET.get('id')
    resultado = -1
    if request.method=="POST":
        #Obtiene los datos del formulario
        formulario=formularioUsuario(request.POST)
        #Comprueba si el formulario es Valido
        if formulario.is_valid():
            #Obtiene La Info del formulario
            infForm = formulario.cleaned_data  
            resultado = models.EditarUsuarios(infForm['username'],infForm['passworduser'],infForm['rol'],idUsuario) 
            Usuarios = models.listarUsuarios()
            if resultado == 1:
                data = {'ListaUsuarios':Usuarios,'resultado': resultado}
                return render(request, "Usuario/editarUsuario.html",data)
            elif resultado == -1:
                data = {'ListaUsuarios':Usuarios,'resultado': resultado}
                return render(request, "Usuario/editarUsuario.html",data) 
    Usuarios = models.listarUsuarios()
    data = {'ListaUsuarios':Usuarios,'resultado': resultado}
    return render(request, "Usuario/editarUsuario.html",data)
#Funcion que muestra 1 Usuario
def DetallesUsuarioHtmx(request):
    idUsuario = request.GET.get('id')
    detallesUsuario = models.DetallesUsuarios(idUsuario)
    for lista in detallesUsuario:
        nombre = lista[1]
        contraseña = lista[2]
        rol = lista[3]
    print(rol)
    DatosFormulario = {
        "username" : nombre,
        "passworduser" : contraseña,
        "rol":rol,
    }
    formularioEditar = formularioUsuario(initial=DatosFormulario)
    data = {'FormularioEditar':formularioEditar,'idUsuario':idUsuario}
    return render(request, "Usuario/detallesUsuario.html",data)
#Funcion para Eliminar Usuario
def EliminarUsuarioHtmx(request):
    idUsuario = request.GET.get('id')
    resultado = models.EliminarUsuarios(idUsuario) 
    Usuarios = models.listarUsuarios()
    print(idUsuario,resultado,Usuarios)
    data = {'ListaUsuarios':Usuarios,'resultado': resultado}
    return render(request, "Usuario/eliminarUsuario.html",data) 
#Modal Eliminar Usuario
def ModalEliminarUsuarioHtmx(request):
    idUsuario = request.GET.get('id')
    data = {'idUsuario':idUsuario} 
    return render(request, "Usuario/modalEliminarUsuario.html",data)
#---------------------------------------------------  Fin vista Usuarios ---------------------------------------------------
#---------------------------------------------------  vista mesero ---------------------------------------------------------
#Funcion que muestra la pagina para administras Mesero
def mesero(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"ADMIN")
    if(logeado and rolCorrecto):
        data = {'Lista':models.listarMeseros(),'form': formularioMesero()}
        return render(request, "Mesero/mesero.html",data)
    else:
        return redirect(linkredireccion)
#Funcion que Agrega Mesero y muestra tabla
def AgregarMeseroHtmx(request):
    resultado = -1
    if request.method=="POST":
        #Obtiene los datos del formulario
        formulario=formularioMesero(request.POST)
        #Comprueba si el formulario es Valido
        if formulario.is_valid():
            #Obtiene La Info del formulario
            infForm = formulario.cleaned_data  
            resultado = models.AgregarMeseros(infForm['rut'],infForm['name1'],infForm['name2'],infForm['lastname1'],infForm['lastname2'])            
            listaResultados = models.listarMeseros()
            if resultado == 1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Mesero/agregarMesero.html",data)
            elif resultado == -1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Mesero/agregarMesero.html",data)
    listaResultados = models.listarMeseros()
    data = {'Lista':listaResultados,'resultado': 0}
    return render(request, "Mesero/agregarMesero.html",data)
#Funcion que muestra 1 Mesero
def DetallesMeseroHtmx(request):
    id = request.GET.get('id')
    detalles = models.DetallesMeseros(id)
    for lista in detalles:  
        rut = lista[1]
        name1 = lista[2]
        name2 = lista[3]
        lastname1 = lista[4]
        lastname2 = lista[5]
    DatosFormulario = {
        "rut" : rut,
        "name1" : name1,
        "name2" : name2,
        "lastname1" : lastname1,
        "lastname2" : lastname2
    }
    formularioEditar = formularioMesero(initial=DatosFormulario)
    data = {'FormularioEditar':formularioEditar,'resultadoid':id}
    return render(request, "Mesero/detallesMesero.html",data)
#Funcion para editar un Mesero
def EditarMeseroHtmx(request):
    id = request.GET.get('id')
    resultado = -1
    if request.method=="POST":
        #Obtiene los datos del formulario
        formulario=formularioMesero(request.POST)
        #Comprueba si el formulario es Valido
        if formulario.is_valid():
            #Obtiene La Info del formulario
            infForm = formulario.cleaned_data  
            resultado = models.EditarMeseros(infForm['rut'],infForm['name1'],infForm['name2'],infForm['lastname1'],infForm['lastname2'],id)   
            listaResultados = models.listarMeseros()
            if resultado == 1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Mesero/editarMesero.html",data)
            elif resultado == -1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Mesero/editarMesero.html",data)
    listaResultados = models.listarMeseros()
    data = {'Lista':listaResultados,'resultado': 0}
    return render(request, "Mesero/editarMesero.html",data)
#Funcion para Eliminar Mesero
def EliminarMeseroHtmx(request):
    try:
        id = request.GET.get('id')
        resultado = models.EliminarMeseros(id) 
        listaResultados = models.listarMeseros()
        data = {'Lista':listaResultados,'resultado': resultado}
        return render(request, "Mesero/eliminarMesero.html",data)
    except:
        data = {'Lista':listaResultados,'resultado': 0}
        return render(request, "Mesero/eliminarMesero.html",data)     
#Modal Eliminar Mesero
def ModalEliminarMeseroHtmx(request):
    id = request.GET.get('id')
    data = {'resultadoid':id} 
    return render(request, "Mesero/modalEliminarMesero.html",data)
#---------------------------------------------------  Fin vista mesero ---------------------------------------------------
#---------------------------------------------------  vista reserva ------------------------------------------------------
#Funcion que muestra la pagina para administras reserva
def reserva(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"ADMIN")
    if(logeado and rolCorrecto):
        data = {'Lista':models.listarReservas(),'form': formularioReserva()}
        return render(request, "Reserva/reserva.html",data)
    else:
        return redirect(linkredireccion)
#Funcion que Agrega reserva y muestra tabla
def AgregarReservaHtmx(request):
    resultado = -1
    if request.method=="POST":
        #Obtiene los datos del formulario
        formulario=formularioReserva(request.POST)
        #Comprueba si el formulario es Valido
        if formulario.is_valid():
            #Obtiene La Info del formulario
            infForm = formulario.cleaned_data
            resultado = models.AgregarReservas(infForm['reservedate'],infForm['reserveHour'],formulario['rt_tableid'].value())            
            listaResultados = models.listarReservas()
            if resultado == 1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Reserva/agregarReserva.html",data)
            elif resultado == -1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Reserva/agregarReserva.html",data)
    listaResultados = models.listarReservas()
    data = {'Lista':listaResultados,'resultado': 0}
    return render(request, "Reserva/agregarReserva.html",data)
#Funcion que muestra 1 reserva
def DetallesReservaHtmx(request):
    id = request.GET.get('id')
    detalles = models.DetallesReservas(id)
    for lista in detalles:  
        rt_tableid = lista[5]
        reservedate = lista[1]
        reservehour = lista[2]
    DatosFormulario = {
        "rt_tableid" : rt_tableid,
        "reservedate" : reservedate,
        "reserveHour" : reservehour
    }
    formularioEditar = formularioReserva(initial=DatosFormulario)
    data = {'FormularioEditar':formularioEditar,'resultadoid':id}
    return render(request, "Reserva/detallesReserva.html",data)
#Funcion para editar un reserva
def EditarReservaHtmx(request):
    id = request.GET.get('id')
    resultado = -1
    if request.method=="POST":
        #Obtiene los datos del formulario
        formulario=formularioReserva(request.POST)
        #Comprueba si el formulario es Valido
        if formulario.is_valid():
            #Obtiene La Info del formulario
            infForm = formulario.cleaned_data  
            resultado = models.EditarReservas(infForm['reservedate'],infForm['reserveHour'],formulario['rt_tableid'].value(),id)   
            listaResultados = models.listarReservas()
            if resultado == 1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Reserva/editarReserva.html",data)
            elif resultado == -1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Reserva/editarReserva.html",data)
    listaResultados = models.listarReservas()
    data = {'Lista':listaResultados,'resultado': 0}
    return render(request, "Reserva/editarReserva.html",data)
#Funcion para Eliminar reserva
def EliminarReservaHtmx(request):
    try:
        id = request.GET.get('id')
        resultado = models.EliminarReservas(id) 
        listaResultados = models.listarReservas()
        data = {'Lista':listaResultados,'resultado': resultado}
        return render(request, "Reserva/eliminarReserva.html",data)
    except:
        data = {'Lista':listaResultados,'resultado': 0}
        return render(request, "Reserva/eliminarReserva.html",data)     
#Modal Eliminar reserva
def ModalEliminarReservaHtmx(request):
    id = request.GET.get('id')
    data = {'resultadoid':id} 
    return render(request, "Reserva/modalEliminarReserva.html",data)
#---------------------------------------------------  Fin vista reserva ----------------------------------------------------
#---------------------------------------------------  vista proveedor ---------------------------------------------------------
#Funcion que muestra la pagina para administras proveedor
def proveedor(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"ADMIN")
    if(logeado and rolCorrecto):
        data = {'Lista':models.listarProveedores(),'form': formularioProveedor()}
        return render(request, "Proveedor/proveedor.html",data)
    else:
        return redirect(linkredireccion)
#Funcion que Agrega proveedor y muestra tabla
def AgregarProveedorHtmx(request):
    resultado = -1
    if request.method=="POST":
        #Obtiene los datos del formulario
        formulario=formularioProveedor(request.POST)
        #Comprueba si el formulario es Valido
        if formulario.is_valid():
            #Obtiene La Info del formulario
            infForm = formulario.cleaned_data  
            resultado = models.AgregarProveedores(infForm['rut'],infForm['companyname'],infForm['name1'],infForm['name2'],infForm['lastname1'],infForm['lastname2'],infForm['region'],infForm['commune'],infForm['direction'],infForm['cellphone'],infForm['mail'])            
            listaResultados = models.listarProveedores()
            if resultado == 1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Proveedor/agregarProveedor.html",data)
            elif resultado == -1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Proveedor/agregarProveedor.html",data)
    listaResultados = models.listarMeseros()
    data = {'Lista':listaResultados,'resultado': 0}
    return render(request, "Proveedor/agregarProveedor.html",data)
#Funcion que muestra 1 proveedor
def DetallesProveedorHtmx(request):
    id = request.GET.get('id')
    detalles = models.DetallesProveedores(id)
    for lista in detalles:  
        rut = lista[1]
        companyname = lista[2]
        name1 =  lista[3]
        name2 = lista[4]
        lastname1 = lista[5]
        lastname2 = lista[6]
        region = lista[7]
        commune = lista[8]
        direction = lista[9]
        cellphone = lista[10]
        mail = lista[11]
    DatosFormulario = {
        'rut' : rut,
        'companyname' : companyname,
        'name1' : name1,
        'name2' : name2,
        'lastname1' : lastname1,
        'lastname2' : lastname2,
        'region' : region,
        'commune' : commune,
        'direction' : direction,
        'cellphone' : cellphone,
        'mail' : mail
    }
    formularioEditar = formularioProveedor(initial=DatosFormulario)
    data = {'FormularioEditar':formularioEditar,'resultadoid':id}
    return render(request, "Proveedor/detallesProveedor.html",data)
#Funcion para editar un proveedor
def EditarProveedorHtmx(request):
    id = request.GET.get('id')
    resultado = -1
    if request.method=="POST":
        #Obtiene los datos del formulario
        formulario=formularioProveedor(request.POST)
        #Comprueba si el formulario es Valido
        if formulario.is_valid():
            #Obtiene La Info del formulario
            infForm = formulario.cleaned_data  
            print("Resultado: "+ str(resultado))
            resultado = models.EditarProveedores(infForm['rut'],infForm['companyname'],infForm['name1'],infForm['name2'],infForm['lastname1'],infForm['lastname2'],infForm['region'],infForm['commune'],infForm['direction'],infForm['cellphone'],infForm['mail'],id)
            print("Resultado: "+ str(resultado))   
            listaResultados = models.listarProveedores()
            if resultado == 1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Proveedor/editarProveedor.html",data)
            elif resultado == -1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Proveedor/editarProveedor.html",data)
    listaResultados = models.listarProveedores()
    data = {'Lista':listaResultados,'resultado': 0}
    return render(request, "Proveedor/editarProveedor.html",data)
#Funcion para Eliminar proveedor
def EliminarProveedorHtmx(request):
    try:
        id = request.GET.get('id')
        resultado = models.EliminarProveedores(id) 
        listaResultados = models.listarProveedores()
        data = {'Lista':listaResultados,'resultado': resultado}
        return render(request, "Proveedor/eliminarProveedor.html",data)
    except:
        data = {'Lista':listaResultados,'resultado': 0}
        return render(request, "Proveedor/eliminarProveedor.html",data)     
#Modal Eliminar proveedor
def ModalEliminarProveedorHtmx(request):
    id = request.GET.get('id')
    data = {'resultadoid':id} 
    return render(request, "Proveedor/modalEliminarProveedor.html",data)
#---------------------------------------------------  Fin vista proveedor ---------------------------------------------------
#---------------------------------------------------  vista Producto ---------------------------------------------------------
#Funcion que muestra la pagina para administras Producto
def producto(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"ADMIN")
    if(logeado and rolCorrecto):
        data = {'Lista':models.listarProductos(),'form': formularioProducto()}
        return render(request, "Producto/producto.html",data)
    else:
        return redirect(linkredireccion)
#Funcion que Agrega Producto y muestra tabla
def AgregarProductoHtmx(request):
    resultado = -1
    if request.method=="POST":
        #Obtiene los datos del formulario
        formulario=formularioProducto(request.POST)
        #Comprueba si el formulario es Valido
        if formulario.is_valid():
            #Obtiene La Info del formulario
            infForm = formulario.cleaned_data  
            resultado = models.AgregarProductos(infForm['purchaseprice'],infForm['stock'],infForm['criticalstock'],infForm['productname'],infForm['productdescription'],formulario['p_idprovider'].value())            
            listaResultados = models.listarProductos()
            if resultado == 1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Producto/agregarProducto.html",data)
            elif resultado == -1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Producto/agregarProducto.html",data)
    listaResultados = models.listarProductos()
    data = {'Lista':listaResultados,'resultado': 0}
    return render(request, "Producto/agregarProducto.html",data)
#Funcion que muestra 1 Producto
def DetallesProductoHtmx(request):
    id = request.GET.get('id')
    detalles = models.DetallesProductos(id)
    for lista in detalles:
        p_idprovider = lista[7]
        purchaseprice = lista[1]
        stock = lista[2]
        criticalstock = lista[3]
        productname = lista[4]
        productdescription = lista[5]
    DatosFormulario = {
        "p_idprovider" : p_idprovider,
        "purchaseprice" : purchaseprice,
        "stock" : stock,
        "criticalstock" : criticalstock,
        "productname" : productname,
        "productdescription" : productdescription
    }
    formularioEditar = formularioProducto(initial=DatosFormulario)
    data = {'FormularioEditar':formularioEditar,'resultadoid':id}
    return render(request, "Producto/detallesProducto.html",data)
#Funcion para editar un Producto
def EditarProductoHtmx(request):
    id = request.GET.get('id')
    resultado = -1
    if request.method=="POST":
        #Obtiene los datos del formulario
        formulario=formularioProducto(request.POST)
        #Comprueba si el formulario es Valido
        if formulario.is_valid():
            #Obtiene La Info del formulario
            infForm = formulario.cleaned_data  
            resultado = models.EditarProductos(infForm['purchaseprice'],infForm['stock'],infForm['criticalstock'],infForm['productname'],infForm['productdescription'],formulario['p_idprovider'].value(),id)  
            listaResultados = models.listarProductos()
            if resultado == 1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Producto/editarProducto.html",data)
            elif resultado == -1:
                data = {'Lista':listaResultados,'resultado': resultado}
                return render(request, "Producto/editarProducto.html",data)
    listaResultados = models.listarProductos()
    data = {'Lista':listaResultados,'resultado': 0}
    return render(request, "Producto/editarProducto.html",data)
#Funcion para Eliminar Producto
def EliminarProductoHtmx(request):
    try:
        id = request.GET.get('id')
        resultado = models.EliminarProductos(id) 
        listaResultados = models.listarProductos()
        data = {'Lista':listaResultados,'resultado': resultado}
        return render(request, "Producto/eliminarProducto.html",data)
    except:
        data = {'Lista':listaResultados,'resultado': 0}
        return render(request, "Producto/eliminarProducto.html",data)     
#Modal Eliminar Producto
def ModalEliminarProductoHtmx(request):
    id = request.GET.get('id')
    data = {'resultadoid':id} 
    return render(request, "Producto/modalEliminarProducto.html",data)
#---------------------------------------------------  Fin vista Producto ---------------------------------------------------