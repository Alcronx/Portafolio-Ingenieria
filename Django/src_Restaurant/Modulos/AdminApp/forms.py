from datetime import date
from django import forms
from django.core import validators
from django.db.models.query import QuerySet
from django.forms import fields, widgets
from django.forms.forms import Form
from Modulos.LoginApp.models import Login
from Modulos.RestaurantApp.models import RestaurantTable,Waiter
from Modulos.BodegaApp.models import Provider,Product 
from django.forms import ValidationError


class DateInput(forms.DateInput):
    input_type = 'date'
     
class formularioUsuario(forms.ModelForm):
 
  class Meta:
        model = Login
        fields = (
            'username',
            'passworduser',
            'rol'
        )
        labels = {
            'username': 'Usuario',
            'passworduser': 'Contraseña',
            'rol': 'Rol'
        }
        widgets = { 
            'username': forms.TextInput(attrs={'class': 'user1' }),
            'passworduser': forms.PasswordInput(attrs={'class': 'user1'}),
            'rol': forms.Select(attrs={'class': 'user1'}),    
        }     
          
class formularioMesa(forms.ModelForm):
    class Meta:
        model = RestaurantTable
        fields = ('tableNumber','tableMembers','aviable')
        labels = {
            'tableNumber': 'Numero Mesa',
            'tableMembers': 'Miembros Mesa',
            'aviable': 'Disponibilidad'
        }
        widgets = {
            'tableNumber': forms.NumberInput(attrs={'class': 'mesa1'}),
            'tableMembers': forms.NumberInput(attrs={'class': 'mesa1'}),
            'aviable': forms.Select(attrs={'class': 'mesa1'}),
        }

class formularioMesero(forms.ModelForm):
    class Meta:
        model = Waiter
        fields = ('rut','name1','name2','lastname1','lastname2')
        labels = {
            'rut': 'Rut',
            'name1': 'Primer Nombre',
            'name2': 'Segundo Nombre',
            'lastname1':'Apellido Paterno',
            'lastname2':'Apellido Materno',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'mesero1'}),
            'name1': forms.TextInput(attrs={'class': 'mesero1'}),
            'name2': forms.TextInput(attrs={'class': 'mesero1'}),
            'lastname1': forms.TextInput(attrs={'class': 'mesero1'}),
            'lastname2': forms.TextInput(attrs={'class': 'mesero1'}),
        } 
            
        

class formularioReserva(forms.Form):

    rt_tableid = forms.ModelChoiceField(queryset=RestaurantTable.objects.filter(state=1),label="ID Mesa", widget=forms.Select(attrs={'class':'reserva1'}))

    reservedate=forms.CharField(
        widget=forms.TextInput(attrs={'type': 'date', 'class': 'reserva1'}),
        label="Fecha Reserva"
    )
    reserveHour=forms.CharField(
        widget=forms.TextInput(attrs={'type': 'time', 'class': 'reserva1'}),
        label="Hora Reserva"
    )

    
  



class formularioProveedor(forms.ModelForm):

    class Meta:
        model = Provider
        fields = ('rut','companyname','name1','name2','lastname1','lastname2','region','commune','direction','cellphone','mail')
        labels = {
            'rut' : 'Rut',
            'companyname': 'Nombre Compañia',
            'name1': 'Primer Nombre',
            'name2': 'Segundo Nombre',
            'lastname1': 'Apellido Paterno',
            'lastname2': 'Apellido Materno',
            'region': 'Region',
            'commune': 'Comuna',
            'direction': 'Direccion',
            'cellphone': 'Telefono',
            'mail': 'Correo',
        }
        widgets = {
            'rut': forms.TextInput(attrs={'class': 'prov1'}),
            'companyname': forms.TextInput(attrs={'class': 'prov1'}),
            'name1': forms.TextInput(attrs={'class': 'prov1'}),
            'name2': forms.TextInput(attrs={'class': 'prov1'}),
            'lastname1': forms.TextInput(attrs={'class': 'prov1'}),
            'lastname2': forms.TextInput(attrs={'class': 'prov1'}),
            'region': forms.TextInput(attrs={'class': 'prov1'}),
            'commune': forms.TextInput(attrs={'class': 'prov1'}),
            'direction': forms.TextInput(attrs={'class': 'prov1'}),
            'cellphone': forms.NumberInput(attrs={'class': 'prov1'}),
            'mail': forms.EmailInput (attrs={'class': 'prov1'}),
        } 

class formularioProducto(forms.ModelForm):
    def __init__(self,*args,**kwargs):
        super (formularioProducto,self).__init__(*args,**kwargs)
        self.fields['p_idprovider'].queryset = Provider.objects.filter(state=1)
    class Meta:
        model = Product
        fields = ('p_idprovider','purchaseprice','stock','criticalstock','productname','productdescription')
        labels = {
            'p_idprovider': 'Nombre Proveedor',
            'purchaseprice': 'Precio Compra',
            'stock': 'Stock',
            'criticalstock': 'Stock Critico',
            'productname': 'Nombre Producto',
            'productdescription': 'Descripcion',
        }
        widgets = {
            'p_idprovider': forms.Select(attrs={'class': 'product1'}),
            'purchaseprice': forms.NumberInput(attrs={'class': 'product1'}),
            'stock': forms.NumberInput(attrs={'class': 'product1'}),
            'criticalstock': forms.NumberInput(attrs={'class': 'product1'}),
            'productname': forms.TextInput(attrs={'class': 'product1'}),
            'productdescription': forms.TextInput(attrs={'class': 'product1'}),
        } 

#Validaciones
    
 



  
  
 













    



  
  
 













    