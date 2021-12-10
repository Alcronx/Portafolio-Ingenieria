from django.urls import path
from Modulos.RestaurantApp.subModulos.cocina import views as CocinaView

urlpatterns = [
    path('', CocinaView.index, name="indexCocina"),
    #----------------------------Urls Ordenes--------------------------
    #----------------Urls Ordenes----------------------------
    path('receta/', CocinaView.receta, name="receta"),
    path('receta/Productos/Agregar', CocinaView.AgregarProductosRecetaHtmx, name="AgregarProductosRecetaHtmx"),
    path('receta/Productos/Eliminar', CocinaView.EliminarProductosRecetaHtmx, name="EliminarProductosRecetaHtmx"),
    path('receta/Productos/Restar', CocinaView.RestarProductosRecetaHtmx, name="RestarProductosRecetaHtmx"),
    path('receta/Productos/Limpiar', CocinaView.LimpiarProductosRecetaHtmx, name="LimpiarProductosRecetaHtmx"),
    path('receta/Productos/Guardar', CocinaView.GuardarDatosProductosRecetaHtmx, name="GuardarDatosProductosRecetaHtmx"),
    path('receta/Productos/ModalGuardar', CocinaView.ModalGuardarDatosProductosRecetanHtmx, name="ModalGuardarDatosProductosRecetanHtmx"),
    #---------------Urls Lista Recetass -------------------------------------------------------------------------------------------------
    path('receta/recetas', CocinaView.recetas, name="recetas"),
    path('receta/recetas/Detalles', CocinaView.DetallesRecetasProductoHtmx, name="DetallesRecetasProductoHtmx"),
    path('receta/recetas/Eliminar', CocinaView.EliminarRecetasProductoHtmx, name="EliminarRecetasProductoHtmx"),
    path('receta/recetas/modaleliminar', CocinaView.ModalEliminarRecetaProductoHtmx, name="ModalEliminarRecetaProductoHtmx"),
    #---------------Urls Tablero -----------------------------------------------------------------------------------------------
    path('tablero/', CocinaView.tablero, name="tablero"),
    path('tablero/CargarRecetasTablero', CocinaView.CargarRecetasTableroHtmx, name="CargarRecetasTablero"),
    path('tablero/TableroOrdenLista', CocinaView.ConfirmarOrdenClienteHtmx, name="ConfirmarOrdenClienteHtmx"),

]



