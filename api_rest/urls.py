"""
URL configuration for api_rest project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from api_rest import views

base = 'api/'

# Aqui es donde vamos a poner los endpoints para poder enviar y recibir informacion en la api
urlpatterns = [
    path(base+"data/", views.getData),
    path(base+"login/", views.login_user),
    path(base+'products/<str:category>', views.getProductsByCategory)
]
