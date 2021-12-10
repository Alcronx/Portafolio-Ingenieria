from django import forms
from Modulos.RestaurantApp.models import Menu
from django.forms import fields, widgets

class formularioMenu(forms.ModelForm):
    cookingtime=forms.CharField(
        widget=forms.TextInput(attrs={'type': 'time', 'class': 'menu1'})
    )
    class Meta:
        model = Menu
        fields = (
            'name','menuprice','recipe',
        )
        labels = {
            'name' : 'Nombre Menu',
            'recipe': 'Receta',
            'menuprice': 'Precio Menu',
        }
        widgets = { 
            'menuprice': forms.NumberInput(attrs={'class': 'margenPrecios'}),
            'recipe': forms.Textarea(attrs={'class': 'menu1'}),
            'name': forms.TextInput(attrs={'class': 'menu1'}),
        }
    field_order = [ 'name','cookingtime','menuprice','recipe']   




    


