from django.db import models
from django.db import connection
import cx_Oracle

#------------------------Funciones Orden-----------------------
def AgregarOrdenCliente(idMesero,idCliente,totalCarritoCliente):   
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_id = cursor.var(cx_Oracle.NUMBER)
    v_Salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("sp_Agregar_OrdenCliente", [idMesero,idCliente,totalCarritoCliente,1,v_id,v_Salida]) 
    return v_Salida.getvalue(),v_id.getvalue()

#------------------------Funciones Detalles Mesa-----------------------
def listarMeserosClienteIonic(v_idcliente):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_MeserosClienteIonic", [v_idcliente,out_cursor])

    lista = []
    datos = ""
    for fila in out_cursor:
        datos =crearJsonMeseros (fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7])
        lista.append(datos)
    
    return lista

def listarOrdenesClientesIonic(v_idcliente):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_OrdenesClientesIonic", [v_idcliente,out_cursor])

    lista = []
    datos = ""
    for fila in out_cursor:
        datos = crearJsonClientes(fila[0],fila[1],fila[2],fila[3],fila[4],fila[5],fila[6],fila[7],fila[8],fila[9])
        lista.append(datos)
    return lista


def crearJsonClientes(ORDECLIENTID,CLIENT_CLIENTID,WAITER_WAITERID,MENUID,QUIANTITY,TOTAL,ORDERCLIENTTOTAL,NAME,STATEORDERSTATE,STATEORDERCLIENT):
    data = {
        "ORDECLIENTID" :ORDECLIENTID,
        "CLIENT_CLIENTID" :CLIENT_CLIENTID,
        "WAITER_WAITERID" :WAITER_WAITERID,
        "MENUID" :MENUID,
        "QUIANTITY" :QUIANTITY,
        "TOTAL" : TOTAL,
        "ORDERCLIENTTOTAL" : ORDERCLIENTTOTAL,
        "NAME" : NAME,
        "STATEORDERSTATE" : STATEORDERSTATE,
        "STATEORDERCLIENT" : STATEORDERCLIENT
    }
    return data

def crearJsonMeseros(WAITERID,CLIENTID,NAMECLIENT,NAMEWAITER,LASTNAMEWAITER,ESTADO_CLIENTE,ESTADO_ORDENCLIENTE,ESTADO_MESERO):
    data = {
        "WAITERID" : WAITERID,
        "CLIENTID" : CLIENTID,
        "NAMECLIENT" : NAMECLIENT,
        "NAMEWAITER" : NAMEWAITER,
        "LASTNAMEWAITER" : LASTNAMEWAITER,
        "ESTADO_CLIENTE" : ESTADO_CLIENTE,
        "ESTADO_ORDENCLIENTE" : ESTADO_ORDENCLIENTE,
        "ESTADO_MESERO" : ESTADO_MESERO,
    }
    return data




def pagarOrdenCliente(id_cliente,id_mesa):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("sp_pagarOdenProducto", [id_cliente,id_mesa,v_Salida])

    return v_Salida.getvalue()





