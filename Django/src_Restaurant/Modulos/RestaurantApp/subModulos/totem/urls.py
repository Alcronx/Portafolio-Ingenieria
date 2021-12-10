from django.urls import path
from Modulos.RestaurantApp.subModulos.totem import views as TotemView

urlpatterns = [
    #----------------------------Urls totem--------------------------
    path('', TotemView.index, name="indexTotem"),
    path('listarMesasTotem', TotemView.listarMesasTotemHtmx, name="listarMesasTotemHtmx"), 
    path('pedirMesaTotem', TotemView.PedirMesaTotemTotemHtmx, name="PedirMesaTotemTotemHtmx"),
    path('comprobarReserva', TotemView.comprobarReservaHtmx, name="comprobarReservaHtmx"),
]