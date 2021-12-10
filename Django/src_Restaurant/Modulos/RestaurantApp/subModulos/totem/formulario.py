from django import forms

class FormularioTotem(forms.Form):

    Nombre=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Nombre Cliente'}))
    Miembros=forms.CharField(widget=forms.NumberInput(attrs={'placeholder': 'Cantidad de Personas'}))