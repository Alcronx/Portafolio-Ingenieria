"""Restaurant URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from Modulos.LoginApp import views as loginView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', loginView.index),
    path('administrador/', include('Modulos.AdminApp.urls')),
    path('bodega/', include('Modulos.BodegaApp.urls')),
    path('finanzas/', include('Modulos.RestaurantApp.subModulos.finanzas.urls')),
    path('cocina/', include('Modulos.RestaurantApp.subModulos.cocina.urls')),
    path('totem/', include('Modulos.RestaurantApp.subModulos.totem.urls')),
    path('RestaurantApi/', include('Modulos.ApiRestaurantApp.urls')),
    path('desconectar/', loginView.desconectar, name="desconectar"),

]


urlpatterns += staticfiles_urlpatterns()
