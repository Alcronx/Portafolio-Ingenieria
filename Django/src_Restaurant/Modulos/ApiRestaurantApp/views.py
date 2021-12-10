from datetime import date
from django.db.models.query import Prefetch
from django.shortcuts import render
from rest_framework import serializers
from rest_framework.response import Response
import json
from Restaurant.settings import REST_FRAMEWORK
from rest_framework.views import APIView
from Modulos.RestaurantApp.models import Menu,Client,Waiter,RestaurantTable,Orderclient
from Modulos.ApiRestaurantApp import models
from .serializer import menuSerializaer,mesaSerializer,meseroSerializaer

class MenuApi(APIView):

    def get(self,request):
        menu1 = Menu.objects.filter(state=1)
        serializer = menuSerializaer(menu1, many=True)
        return Response(serializer.data)

class ClienteApi(APIView):

    def get(self,request):
        cliente = RestaurantTable.objects.filter(state=1,aviable=0).prefetch_related(Prefetch("rt_tableid_related",queryset=Client.objects.filter(state=1).order_by('-clientid')))
        serializer = mesaSerializer(cliente, many=True)
        return Response(serializer.data)

class MeseroApi(APIView):

    def get(self,request):
        mesero = Waiter.objects.filter(state=1)
        serializer = meseroSerializaer(mesero, many=True)
        return Response(serializer.data)

class OrdenApi(APIView):
    def post(self,request):
        data = json.dumps(request.data)
        stringData = "["+data+"]"
        listData = json.loads(stringData)
        idMesero = listData[0]["idMesero"]
        idCliente = listData[0]["idCliente"]
        totalCarritoCliente = listData[0]["totalCarrito"]
        try:
            resultadoAOP,idOrden = models.AgregarOrdenCliente(idMesero,idCliente,totalCarritoCliente)
            if resultadoAOP == 1:
                #Crea Lista Menu
                listCarrito = []
                for i in listData[0]["OrderClientDetails"]:
                    carrito = Orderclient.menus.through(ocdorderclientid=Orderclient.objects.get(ordeclientid=idOrden),ocdmenuid=Menu.objects.get(menuid=i["menuid"]),quiantity=i["quantity"],total=i["total"])
                    listCarrito.append(carrito)
                Orderclient.menus.through.objects.bulk_create(listCarrito)
                return Response(1)
            return Response(0)
        except:
                return Response(-1)


class DetallesMesaApi(APIView):
    def post(self,request):
        try:
            data = json.dumps(request.data)
            if not(data == "{}"):
                stringData = "["+data+"]"
                listData = json.loads(stringData)
                opcion =listData[0]["Opcion"]
                idCliente =listData[0]["idCliente"]
                #Opcion 1 es para obtener Datos Mesero
                if (opcion == "1"):   
                    meseros = []
                    meseros = models.listarMeserosClienteIonic(idCliente)
                    return Response(meseros)
                #Opcion 2 es para obtener DetallesOrdenCliente
                elif (opcion == "2"):
                    detallesOrden = models.listarOrdenesClientesIonic(idCliente)
                    return Response(detallesOrden)
                else:
                    return Response(0)
            else:
                return Response(0)
        except:
            return Response(-1)


class PagarOrdenApi(APIView):
    def post(self,request):
        data = json.dumps(request.data)
        stringData = "["+data+"]"
        listData = json.loads(stringData)
        idMesa = listData[0]["idMesa"]
        idCliente = listData[0]["idCliente"]
        try:
            resultadoAOP = models.pagarOrdenCliente(idCliente,idMesa)
            if resultadoAOP == 1:
                return Response(1)
            return Response(0)
        except:
                return Response(-1)

        
    










