from rest_framework import serializers
from .models import *


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['id', 'tipo_rol']


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Data
        fields = ['id', 'usd_clp', 'fecha_actualizacion']


class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuarios
        fields = ['id', 'usuario', 'passw']


class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'


class UpdateProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = ['id', 'nom_producto', 'precio', 'precio_ofer', 'imagen', 'stock', 'desc',
                  'color', 'trastes', 'mat_cuerpo', 'mat_neck', 'mat_fingerb', 'marca', 'categoria']


class CategorySearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = ['id', 'nom_categoria']


class MarcasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Marcas
        fields = '__all__'


class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorias
        fields = '__all__'
