from django import forms
from django.db.models.query import QuerySet
from Modulos.BodegaApp.models import Product 



class formularioStockProducto(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('stock','criticalstock')
        labels = {
            'stock': 'Stock',
            'criticalstock': 'Stock Critico',
        }

        widgets = { 
            'stock': forms.NumberInput(attrs={'class': 'bodega1'}),
            'criticalstock': forms.NumberInput(attrs={'class': 'bodega1'}),   
        }
