from django.db.models import fields
from rest_framework import serializers
from Modulos.RestaurantApp.models import Menu,Client,Waiter,RestaurantTable



class menuSerializaer(serializers.ModelSerializer):
    class Meta: 
        model = Menu
        fields = '__all__'

class clienteSerializaer(serializers.ModelSerializer):
    class Meta: 
        model = Client
        fields = '__all__'

class mesaSerializer(serializers.ModelSerializer):
    class Meta: 
        model = RestaurantTable
        fields = 'tableid','tableNumber','tableMembers','aviable','state','rt_tableid_related'
    rt_tableid_related = clienteSerializaer(many=True)

class meseroSerializaer(serializers.ModelSerializer):
    class Meta: 
        model = Waiter
        fields = '__all__'






    








    