from django.db import models
from django.db import connection
import cx_Oracle

class Provider(models.Model):
    idprovider = models.AutoField(primary_key=True)
    rut = models.CharField(max_length=10)
    companyname = models.CharField(max_length=30)
    name1 = models.CharField(max_length=30)
    name2 = models.CharField(max_length=30)
    lastname1 = models.CharField(max_length=30)
    lastname2 = models.CharField(max_length=30)
    region = models.CharField(max_length=50)
    commune = models.CharField(max_length=50)
    direction = models.CharField(max_length=70)
    cellphone = models.IntegerField()
    mail = models.CharField(max_length=50)
    state = models.CharField(max_length=1)
    class Meta:
        db_table = "Provider"
    def __str__(self):
        return self.companyname


class Product(models.Model):
    productid = models.AutoField(primary_key=True)
    purchaseprice = models.IntegerField()
    stock = models.IntegerField()
    criticalstock = models.IntegerField()
    productname = models.CharField(max_length=30)
    productdescription = models.CharField(max_length=30)
    state = models.CharField(max_length=1)
    p_idprovider = models.ForeignKey(Provider,on_delete=models.CASCADE,db_column='p_idprovider')
    class Meta:
        db_table = "Product"


class Orderproduct(models.Model):
    orderproductid = models.AutoField(primary_key=True)
    orderdate = models.DateField()
    orderhour = models.DateField()
    receptiondate = models.DateField(blank=True, null=True)
    receptionhour = models.DateField(blank=True, null=True)
    totalorderproduct = models.BigIntegerField(blank=True, null=True)
    products = models.ManyToManyField(Product, through="Orderproductdetails")
    state = models.CharField(max_length=1)
    class Meta:
        db_table = 'Orderproduct'


class Orderproductdetails(models.Model):
    opdproductid = models.ForeignKey(Product,on_delete=models.CASCADE,db_column='opdproductid')
    opdorderproductid = models.ForeignKey(Orderproduct,on_delete=models.CASCADE,db_column='opdorderproductid')
    quantity = models.IntegerField()
    total = models.BigIntegerField()

    class Meta:
        db_table = 'Orderproductdetails'
        unique_together = ('opdproductid','opdorderproductid')


def ListarProveedorescbx():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_COMBOBOX_PROVEEDOR", [out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

def ProductosProveedores(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("SP_LISTAR_PRODUCTOS_PROVEEDOR", [id,out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista


#------------------------Funciones Orden-----------------------
def AgregarOrdenProducto(totalorderproduct):   
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_id = cursor.var(cx_Oracle.NUMBER)
    v_Salida = cursor.var(cx_Oracle.NUMBER)
    cursor.callproc("SP_AGREGAR_ORDENPRODUCTO", [totalorderproduct,1,v_id,v_Salida])
    return v_Salida.getvalue(),v_id.getvalue()

def EliminarOrdenProducto(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("SP_ELIMINARORDENPRODUCTO", [id,v_Salida])

    return v_Salida.getvalue()

def listarOrdenesProducto():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_OrdenesProducto", [out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista


def listarOrdenesProductoDetalles(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_OrdenesProductoDetalle", [id,out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista

def ConfirmarOrdenProducto(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("sp_ConfirmarOrdenProducto", [id,v_Salida])

    return v_Salida.getvalue()

def DesconfirmarOrdenProducto(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("sp_DesconfirmarOrdenProducto", [id,v_Salida])

    return v_Salida.getvalue()


#------------------------Funciones Stock Productos-----------------------
def listarStocksProducto():
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("sp_listar_StockProductos", [out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista


def EditarStocksProductos(stock,criticalstock,id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    v_Salida = cursor.var(cx_Oracle.NUMBER)

    cursor.callproc("sp_EditarStockProducto", [id,stock,criticalstock,v_Salida])

    return v_Salida.getvalue()


def DetallesStocksProductos(id):
    django_cursor = connection.cursor()
    cursor = django_cursor.connection.cursor()
    out_cursor = django_cursor.connection.cursor()

    cursor.callproc("sp_DetallesStockProducto", [id,out_cursor])

    lista = []

    for fila in out_cursor:
        lista.append(fila)
    
    return lista



