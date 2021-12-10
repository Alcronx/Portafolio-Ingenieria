from django.db import connection
import cx_Oracle


#---------------------FUNCIONES Usuario--------------------
def listarUsuarios():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_USUARIOS", [out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

def AgregarUsuarios(username,password,rol):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_AGREGAR_USUARIOS", [username,password,rol,1,v_Salida])

    return v_Salida.getvalue()

def EditarUsuarios(username,password,rol,id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_EDITARUSUARIO", [id,username,password,rol,v_Salida])

    return v_Salida.getvalue()

def EliminarUsuarios(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_ELIMINARUSUARIO", [id,v_Salida])

    return v_Salida.getvalue()

def DetallesUsuarios(idUsuario):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("SP_DETALLESUSUARIO", [idUsuario,out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

#------------------------Funciones Mesa-----------------------
def listarMesas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_MESAS", [out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

def AgregarMesas(tableNumber,tableMembers,aviable):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_AGREGAR_MESA", [tableNumber,tableMembers,aviable,1,v_Salida])
    return v_Salida.getvalue()

def EditarMesas(tableNumber,tableMembers,aviable,id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_EDITARMESA", [id,tableNumber,tableMembers,aviable,v_Salida])

    return v_Salida.getvalue()

def EliminarMesas(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_ELIMINARMESA", [id,v_Salida])

    return v_Salida.getvalue()

def DetallesMesas(idUsuario):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("SP_DETALLESMESA", [idUsuario,out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

#------------------------Funciones Mesero-----------------------
def listarMeseros():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_MESEROS", [out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

def AgregarMeseros(rut,name1,name2,lastname1,lastname2):   
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_AGREGAR_MESERO", [rut,name1,name2,lastname1,lastname2,1,v_Salida])
    return v_Salida.getvalue()

def EditarMeseros(rut,name1,name2,lastname1,lastname2,id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_EDITARMESERO", [id,rut,name1,name2,lastname1,lastname2,v_Salida])

    return v_Salida.getvalue()

def EliminarMeseros(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_ELIMINARMESERO", [id,v_Salida])

    return v_Salida.getvalue()

def DetallesMeseros(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("SP_DETALLESMESERO", [id,out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

#------------------------Funciones reserva-----------------------
def listarReservas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_RESERVAS", [out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

def AgregarReservas(reservedate,reservehour,rt_tableid):   
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_AGREGAR_RESERVA", [str(reservedate),str(reservehour),str(rt_tableid),1,v_Salida])
    return v_Salida.getvalue()

def EditarReservas(reservedate,reservehour,rt_tableid,id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_EDITARRESERVA", [id,reservedate,reservehour,rt_tableid,v_Salida])

    return v_Salida.getvalue()

def EliminarReservas(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_ELIMINARRESERVA", [id,v_Salida])

    return v_Salida.getvalue()

def DetallesReservas(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("SP_DETALLESRESERVA", [id,out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

#------------------------Funciones Proveedores-----------------------
def listarProveedores():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PROVEEDORES", [out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

def AgregarProveedores(rut,companyname,name1,name2,lastname1,lastname2,region,commune,direction,cellphone,mail):   
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_AGREGAR_PROVEEDOR", [rut,companyname,name1,name2,lastname1,lastname2,region,commune,direction,cellphone,mail,1,v_Salida])
    return v_Salida.getvalue()

def EditarProveedores(rut,companyname,name1,name2,lastname1,lastname2,region,commune,direction,cellphone,mail,id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_EDITARPROVEEDOR", [id,rut,companyname,name1,name2,lastname1,lastname2,region,commune,direction,cellphone,mail,v_Salida])
    return v_Salida.getvalue()

def EliminarProveedores(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_ELIMINARPROVEEDOR", [id,v_Salida])

    return v_Salida.getvalue()

def DetallesProveedores(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("SP_DETALLESPROVEEDOR", [id,out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

#------------------------Funciones Productos-----------------------
def listarProductos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRODUCTOS", [out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

def AgregarProductos(purchaseprice,stock,criticalstock,productname,productdescription,p_idprovider):   
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_AGREGAR_PRODUCTO", [purchaseprice,stock,criticalstock,productname,productdescription,1,p_idprovider,v_Salida])
    return v_Salida.getvalue()

def EditarProductos(purchaseprice,stock,criticalstock,productname,productdescription,p_idprovider,id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_EDITARPRODUCTO", [id,purchaseprice,stock,criticalstock,productname,productdescription,p_idprovider,v_Salida])

    return v_Salida.getvalue()

def EliminarProductos(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_ELIMINARPRODUCTO", [id,v_Salida])

    return v_Salida.getvalue()

def DetallesProductos(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("SP_DETALLESPRODUCTO", [id,out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

#Funciones Reporte Administrador

def mostrarMenusVendidosDia():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("sp_Menus_vendidos_Dia", [out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

def mostrarProductosOrdenadosDia():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("sp_Productos_ordenados_Dia", [out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

def mostrarGananciaMenuDia():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("sp_Ganancia_Menu_Dia", [out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

 


