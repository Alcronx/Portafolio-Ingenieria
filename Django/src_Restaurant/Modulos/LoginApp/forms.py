from django import forms

class FormularioLogin(forms.Form):

    nombre=forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','placeholder': 'Nombre'}))
    contrasena=forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control','placeholder': 'Contraseña'}))
