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
