from django.shortcuts import render
from django.shortcuts import render,redirect, resolve_url
from Modulos.LoginApp.views import ComprobarUsuario
from Modulos.RestaurantApp import models

# Create your views here.

def index(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"FINANZAS")
    if(logeado and rolCorrecto):
        return render(request, "finanzas/indexFinanzas.html")
    else:
        return redirect(linkredireccion)
    

def finanzas(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"FINANZAS")
    if(logeado and rolCorrecto):
        data = {'Lista1':models.mostrarBoletas(),'Lista2':models.mostrarGananciaMenuDiaFianzas()}
        return render(request, "finanzas/finanzas.html",data)
    else:
        return redirect(linkredireccion)
    







