from django.urls import path
from Modulos.RestaurantApp.subModulos.finanzas import views as finanzasView

urlpatterns = [
    path('', finanzasView.index, name="indexFinanzas"),
    path('finanzas/', finanzasView.finanzas, name="finanzas"),

]