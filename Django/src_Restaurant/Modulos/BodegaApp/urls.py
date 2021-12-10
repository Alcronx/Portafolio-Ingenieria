from django.urls import path
from Modulos.BodegaApp import views as bodegaView

urlpatterns = [
    path('', bodegaView.index, name="indexBodega"),
    #----------------Urls Ordenes----------------------------
    path('orden/', bodegaView.orden, name="orden"),
    path('orden/Productos', bodegaView.ListarProductosOrdenHtmx, name="ListarProductosOrdenHtmx"),
    path('orden/Productos/Agregar', bodegaView.AgregarProductosOrdenHtmx, name="AgregarProductosOrdenHtmx"),
    path('orden/Productos/Eliminar', bodegaView.EliminarProductosOrdenHtmx, name="EliminarProductosOrdenHtmx"),
    path('orden/Productos/Restar', bodegaView.RestarProductosOrdenHtmx, name="RestarProductosOrdenHtmx"),
    path('orden/Productos/Limpiar', bodegaView.LimpiarProductosOrdenHtmx, name="LimpiarProductosOrdenHtmx"),
    path('orden/Productos/Guardar', bodegaView.GuardarDatosProductosOrdenHtmx, name="GuardarDatosProductosOrdenHtmx"),
    path('orden/ordenes', bodegaView.ordenes, name="ordenes"),
    path('orden/ordenes/Detalles', bodegaView.DetallesOrdenesProductoHtmx, name="DetallesOrdenesProductoHtmx"),
    path('orden/ordenes/Eliminar', bodegaView.EliminarOrdenesProductoHtmx, name="EliminarOrdenesProductoHtmx"),
    path('orden/ordenes/Confirmar', bodegaView.ConfirmarOrdenesProductoHtmx, name="ConfirmarOrdenesProductoHtmx"),
    path('orden/ordenes/modaleliminar', bodegaView.ModalEliminarOrdenProductoHtmx, name="ModalEliminarOrdenProductoHtmx"),
    path('orden/ordenes/Desconfirmar', bodegaView.DesconfirmarOrdenesProductoHtmx, name="DesconfirmarOrdenesProductoHtmx"),
    #-----------------Fin ulrs Orden---------------------------------------------------
    #----------Stock Productos----------
    path('stockproducto/', bodegaView.stockproducto, name="stockproducto"),
    path('stockproducto/Detalles', bodegaView.DetallesStockProductoHtmx, name="DetallesStockProductoHtmx"),
    path('stockproducto/editar', bodegaView.EditarStockProductoHtmx, name="EditarStockProductoHtmx"), 
    #----------Fin Stock Productos----------

]


