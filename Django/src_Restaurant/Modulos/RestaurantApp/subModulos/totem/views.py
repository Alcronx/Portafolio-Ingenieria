from django.http.response import HttpResponse
from django.shortcuts import render,redirect, resolve_url
from Modulos.LoginApp.views import ComprobarUsuario
from Modulos.RestaurantApp import models
from Modulos.RestaurantApp.subModulos.totem.formulario import FormularioTotem

def index(request):
    logeado,rolCorrecto,linkredireccion = ComprobarUsuario(request,"TOTEM")
    if(logeado and rolCorrecto):
        formularioLogin=FormularioTotem()
        data = {"form":formularioLogin}
        return render(request, "totem/indexTotem.html", data)
    else:
        return redirect(linkredireccion)

def listarMesasTotemHtmx(request):
    Nombre = request.POST.get('Nombre')
    Miembros = request.POST.get('Miembros')
    data = {'radioMesas':models.ListarRadioMesas(Miembros),"NombreCliente":Nombre,"Miembros":Miembros} 
    return render(request, "totem/listarMesasTotem.html", data)
             
def PedirMesaTotemTotemHtmx(request):
    Nombre = request.POST.get('Nombre')
    Miembros = request.POST.get('Miembros')
    RadioMesas = request.POST.get('RadioMesas')
    resultado = models.AgregarClienteTotem(Nombre,Miembros,RadioMesas)
    print(resultado)
    data = {'resultado':resultado} 
    return render(request, "totem/pedirMesaTotem.html",data)

def comprobarReservaHtmx(request):
    try:
        Nombre = request.POST.get('NombreClienteTotem')
        idReserva = request.POST.get('idReservaTotem')
        resultadoConsulta = models.Reserved.objects.filter(reserveid=idReserva,state=1).exists()
        if resultadoConsulta:
            obj = models.Reserved.objects.get(reserveid=idReserva,state=1)
            idMesa = getattr(obj,'rt_tableid_id')
            obj2 = models.RestaurantTable.objects.get(tableid=str(idMesa),state=1)
            numeroMesa = getattr(obj2,'tableNumber')
            data = {'resultado':1,'nombre':Nombre,'numeroMesa':numeroMesa} 
        else:
            data = {'resultado':0,'nombre':Nombre}
        
        return render(request, "totem/comprobarReservTotem.html", data)
    except Exception as e:
        print(e)
        data = {'resultado':0,'nombre':Nombre}
        return render(request, "totem/comprobarReservTotem.html", data)




    






