from rest_framework import serializers
from .models import *


class RolesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Roles
        fields = ['id', 'tipo_rol']
