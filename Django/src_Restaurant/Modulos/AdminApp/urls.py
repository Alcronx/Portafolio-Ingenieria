from django.urls import path
from Modulos.AdminApp import views as adminView

urlpatterns = [
#----------Pagin Principal Admin----------
    path('', adminView.index, name="indexAdmin"),
#----------Mesa----------
    path('mesa/', adminView.mesa, name="mesa"),
    path('mesa/agregar', adminView.AgregarMesaHtmx, name="AgregarMesaHtmx"),
    path('mesa/Detalles', adminView.DetallesMesaHtmx, name="DetallesMesaHtmx"),
    path('mesa/editar', adminView.EditarMesaHtmx, name="EditarMesaHtmx"),
    path('mesa/eliminar', adminView.EliminarMesaHtmx, name="EliminarMesaHtmx"),
    path('mesa/modaleliminar', adminView.ModalEliminarMesaHtmx, name="modalEliminarMesaHtmx"),
#----------reporte----------
    path('reporte/', adminView.reporte, name="reporte"),
#----------Usuarios----------
    path('usuario/', adminView.usuario, name="usuario"),
    path('usuario/agregar', adminView.AgregarUsuarioHtmx, name="AgregarUsuarioHtmx"),
    path('usuario/Detalles', adminView.DetallesUsuarioHtmx, name="DetallesUsuarioHtmx"),
    path('usuario/editar', adminView.EditarUsuarioHtmx, name="EditarUsuarioHtmx"),
    path('usuario/eliminar', adminView.EliminarUsuarioHtmx, name="EliminarUsuarioHtmx"),
    path('usuario/modaleliminar', adminView.ModalEliminarUsuarioHtmx, name="modalEliminarUsuarioHtmx"),
#----------Mesero----------
    path('mesero/', adminView.mesero, name="mesero"),
    path('mesero/agregar', adminView.AgregarMeseroHtmx, name="AgregarMeseroHtmx"),
    path('mesero/Detalles', adminView.DetallesMeseroHtmx, name="DetallesMeseroHtmx"),
    path('mesero/editar', adminView.EditarMeseroHtmx, name="EditarMeseroHtmx"), 
    path('mesero/eliminar', adminView.EliminarMeseroHtmx, name="EliminarMeseroHtmx"),
    path('mesero/modaleliminar', adminView.ModalEliminarMeseroHtmx, name="modalEliminarMeseroHtmx"),
#----------Reserva----------
    path('reserva/', adminView.reserva, name="reserva"),
    path('reserva/agregar', adminView.AgregarReservaHtmx, name="AgregarReservaHtmx"),
    path('reserva/Detalles', adminView.DetallesReservaHtmx, name="DetallesReservaHtmx"),
    path('reserva/editar', adminView.EditarReservaHtmx, name="EditarReservaHtmx"), 
    path('reserva/eliminar', adminView.EliminarReservaHtmx, name="EliminarReservaHtmx"),
    path('reserva/modaleliminar', adminView.ModalEliminarReservaHtmx, name="modalEliminarReservaHtmx"),
#----------Proveedor----------
    path('proveedor/', adminView.proveedor, name="proveedor"),
    path('proveedor/agregar', adminView.AgregarProveedorHtmx, name="AgregarProveedorHtmx"),
    path('proveedor/Detalles', adminView.DetallesProveedorHtmx, name="DetallesProveedorHtmx"),
    path('proveedor/editar', adminView.EditarProveedorHtmx, name="EditarProveedorHtmx"), 
    path('proveedor/eliminar', adminView.EliminarProveedorHtmx, name="EliminarProveedorHtmx"),
    path('proveedor/modaleliminar', adminView.ModalEliminarProveedorHtmx, name="modalEliminarProveedorHtmx"),
#----------Producto----------
    path('producto/', adminView.producto, name="producto"),
    path('producto/agregar', adminView.AgregarProductoHtmx, name="AgregarProductoHtmx"),
    path('producto/Detalles', adminView.DetallesProductoHtmx, name="DetallesProductoHtmx"),
    path('producto/editar', adminView.EditarProductoHtmx, name="EditarProductoHtmx"), 
    path('producto/eliminar', adminView.EliminarProductoHtmx, name="EliminarProductoHtmx"),
    path('producto/modaleliminar', adminView.ModalEliminarProductoHtmx, name="modalEliminarProductoHtmx"),
]



