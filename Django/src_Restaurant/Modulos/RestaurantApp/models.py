from django.db import models
from Modulos.BodegaApp.models import Product
from Modulos.RestaurantApp.choice import DISPONIBILIDAD
import cx_Oracle
from django.db import connection

class RestaurantTable(models.Model):
    tableid = models.AutoField(primary_key=True)
    tableNumber = models.IntegerField()
    tableMembers = models.IntegerField()
    aviable = models.CharField(max_length=1,choices=DISPONIBILIDAD,default="DISPONIBLE")
    state = models.CharField(max_length=1)
    class Meta:
        db_table = 'RestaurantTable'
    def __str__(self):
        return  str(self.tableNumber)
        

class Client(models.Model):
    clientid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    members = models.IntegerField()
    state = models.CharField(max_length=1)
    rt_tableid = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE, db_column='rt_tableid',related_name='rt_tableid_related')

    class Meta:
        db_table = 'Client'

class Reserved(models.Model):
    reserveid = models.AutoField(primary_key=True)
    reservedate = models.DateField()
    reservehour = models.DateField()
    state = models.CharField(max_length=1)
    rt_tableid = models.ForeignKey(RestaurantTable, on_delete=models.CASCADE, db_column='rt_tableid')

    class Meta:
        db_table = 'Reserved'

class Waiter(models.Model):
    waiterid = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=10)
    name1 = models.CharField(max_length=50)
    name2 = models.CharField(max_length=50)
    lastname1 = models.CharField(max_length=50)
    lastname2 = models.CharField(max_length=50)
    state = models.CharField(max_length=1)

    class Meta:
        db_table = 'waiter'

class Menu(models.Model):
    menuid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    recipe = models.CharField(max_length=1000)
    cookingtime = models.DateField()
    menucost = models.BigIntegerField(blank=True, null=True)
    menuprice = models.BigIntegerField()
    state = models.CharField(max_length=1)
    products = models.ManyToManyField(Product, through="Productmenu")

    class Meta:
        db_table = 'Menu'
        
class Orderclient(models.Model):
    ordeclientid = models.AutoField(primary_key=True)
    orderhour = models.DateField()
    orderdate = models.DateField()
    orderclienttotal = models.BigIntegerField(blank=True, null=True)
    state = models.CharField(max_length=1)
    client_clientid = models.ForeignKey(Client, on_delete=models.CASCADE, db_column='client_clientid')
    waiter_waiterid = models.ForeignKey(Waiter, on_delete=models.CASCADE, db_column='waiter_waiterid')
    menus = models.ManyToManyField(Menu, through="Orderclientdetails")

    class Meta:
        db_table = 'Orderclient'


class Orderclientdetails(models.Model):
    ocdorderclientid = models.ForeignKey(Orderclient,on_delete=models.CASCADE, db_column='ocdorderclientid')
    ocdmenuid = models.ForeignKey(Menu,on_delete=models.CASCADE, db_column='ocdmenuid')
    quiantity = models.IntegerField()
    total = models.BigIntegerField()

    class Meta:
        db_table = 'OrderClientDetails'
        unique_together = ('ocdorderclientid', 'ocdmenuid')



class Productmenu(models.Model):
    pmmenuid = models.ForeignKey(Menu,on_delete=models.CASCADE, db_column='pmmenuid')
    pmproductid = models.ForeignKey(Product,on_delete=models.CASCADE, db_column='pmproductid')
    quantity = models.IntegerField()
    total = models.BigIntegerField()

    class Meta:
        db_table = 'ProductMenu'
        unique_together = ('pmmenuid', 'pmproductid')



#-------------------------Funciones Sp -----------------------------------
#-------------------------Menus-------------------------------------------
def listarProductos():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRODUCTOS", [out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

def AgregarMenuProducto(name,recipe,cookingtime,menucost,menuprice):   
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_id = cursor.var(cx_Oracle.NUMBER)
    v_Salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_AGREGAR_MENUPRODUCTO", [recipe,cookingtime,menucost,menuprice,name,1,v_id,v_Salida])
    return v_Salida.getvalue(),v_id.getvalue()

#------------------------Funciones Menu-----------------------
def EliminarMenuProducto(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("sp_EliminarMenuProducto", [id,v_Salida])

    return v_Salida.getvalue()

def listarMenusProducto():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_MenusProducto", [out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista


def listarMenusProductoDetalles(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_ProductoDetalle", [id,out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

#------------------------Funciones Tablero Cocina-----------------------

def listarOrdenesClienteTablero():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()
    cursor.callproc("sp_listar_OrdenesClientes", [out_cursor])
    lista = []
    contador = 0
    for fila in out_cursor:
        contador = contador+1
        fila2 = fila+(contador,)
        lista.append(fila2)
    return lista

def listarDetallesOrdenesClienteTablero(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()
    cursor.callproc("sp_listar_DetallesOrdenesClientes", [id,out_cursor])
    lista = []
    for fila in out_cursor:
        lista.append(fila)   
    return lista


def ConfirmarOrdenCliente(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("sp_ConfirmarOrdenCliente", [id,v_Salida])

    return v_Salida.getvalue()


#------------------------Funciones Totem-----------------------

def ListarRadioMesas(Miembros):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()
    cursor.callproc("sp_listar_MesasTotemCliente", [Miembros,out_cursor])

    lista = []
    contador = 0
    for fila in out_cursor:
       contador = contador+1
       fila2 = fila+(contador,)
       lista.append(fila2)
    
    return lista


def AgregarClienteTotem(Nombre,miembros,idMesa):   
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_AGREGAR_CLIENTE", [Nombre,miembros,1,idMesa,v_Salida])
    return v_Salida.getvalue()


#Funciones finanzas

def mostrarGananciaMenuDiaFianzas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("sp_Ganancia_Menu_Dia", [out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista


def mostrarBoletas():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("sp_Boletas", [out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista
    