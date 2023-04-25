from django.db import models


class UsuarioCliente(models.Model):
    nombre = models.CharField(max_length=30)
    correo = models.CharField(max_length=50)
