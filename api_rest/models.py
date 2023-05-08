from django.db import models


class Roles(models.Model):
    tipo_rol = models.CharField(max_length=50)


class Personas(models.Model):
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250, null=True)
    rut = models.CharField(max_length=20, null=True, unique=True)
    tel = models.CharField(max_length=30)


class Data(models.Model):
    usd_clp = models.FloatField()
    fecha_actualizacion = models.DateField()


class Categorias(models.Model):
    nom_categoria = models.CharField(max_length=200)
    foto = models.BinaryField()
    desc = models.CharField(max_length=2500)


class Marcas(models.Model):
    nom_marca = models.CharField(max_length=150)
    pais = models.CharField(max_length=150)


class Usuarios(models.Model):
    usuario = models.CharField(max_length=80, unique=True)
    correo = models.CharField(max_length=200, unique=True)
    passw = models.CharField(max_length=255)
    persona = models.ForeignKey(
        Personas, on_delete=models.CASCADE, unique=True)
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE, unique=True)


class Compras(models.Model):
    fecha_compra = models.DateField()
    total = models.IntegerField()
    tipo_compra = models.BooleanField()
    usuario = models.ForeignKey(
        Usuarios, on_delete=models.CASCADE, null=True, unique=False)


class Productos(models.Model):
    nom_producto = models.CharField(max_length=200)
    precio = models.IntegerField()
    precio_ofer = models.IntegerField(null=True)
    imagen = models.BinaryField(null=True)
    stock = models.IntegerField()
    fecha_creacion = models.DateField()
    desc = models.CharField(max_length=2500)

    color = models.CharField(max_length=150, null=True)
    trastes = models.CharField(max_length=150, null=True)
    mat_cuerpo = models.CharField(max_length=150, null=True)
    mat_neck = models.CharField(max_length=150, null=True)
    mat_fingerb = models.CharField(max_length=150, null=True)

    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)


class Rel_Prod_Comp(models.Model):
    producto = models.ForeignKey(
        Productos, on_delete=models.CASCADE, unique=False)
    compra = models.ForeignKey(Compras, on_delete=models.CASCADE, unique=True)
    cantidad = models.IntegerField()
