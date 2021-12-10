from django.urls import path
from Modulos.ApiRestaurantApp import views as apiView
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('Menu', apiView.MenuApi.as_view(), name="ApiMenu"),
    path('Cliente', apiView.ClienteApi.as_view(), name="ApiMesa"),
    path('Mesero', apiView.MeseroApi.as_view(), name="ApiMesero"),
    path('Orden', apiView.OrdenApi.as_view(), name="ApiOrden"),
    path('DetallesMesa', apiView.DetallesMesaApi.as_view(), name="ApiDetallesMesa"),
    path('PagarOrdenApi', apiView.PagarOrdenApi.as_view(), name="ApiPagarOrden"),
    

]