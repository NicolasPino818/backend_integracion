from django.db import models


class Roles(models.Model):
    tipo_rol = models.CharField(max_length=50)

    def __str__(self):
        return self.tipo_rol


class Categorias(models.Model):
    nom_categoria = models.CharField(max_length=200)

    def __str__(self):
        return self.nom_categoria


class Data(models.Model):
    usd_clp = models.IntegerField()
    fecha_actualizacion = models.DateField()

    def __str__(self):
        return self


class Marcas(models.Model):
    nom_marca = models.CharField(max_length=150)
    pais = models.CharField(max_length=150)


class Personas(models.Model):
    nombres = models.CharField(max_length=250)
    apellidos = models.CharField(max_length=250, null=True)
    rut = models.CharField(max_length=20, null=True)
    tel = models.CharField(max_length=30)


class Usuarios(models.Model):
    usuario = models.CharField(max_length=90)
    correo = models.CharField(max_length=200)
    passw = models.CharField(max_length=255)
    persona = models.ForeignKey(Personas, on_delete=models.CASCADE)
    rol = models.ForeignKey(Roles, on_delete=models.CASCADE)


class Productos(models.Model):
    nom_producto = models.CharField(max_length=200)
    precio = models.IntegerField()
    precio_oferta = models.IntegerField(null=True)
    imagen = models.BinaryField(null=True)
    fecha_creacion = models.DateField()
    descripcion = models.CharField(max_length=2500)
    color = models.CharField(max_length=150, null=True)
    trastes = models.CharField(max_length=150, null=True)
    mat_cuerpo = models.CharField(max_length=150, null=True)
    mat_neck = models.CharField(max_length=150, null=True)
    mat_fingerb = models.CharField(max_length=150, null=True)

    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    marca = models.ForeignKey(Marcas, on_delete=models.CASCADE)


class Compras(models.Model):
    fecha_compra = models.DateField()
    total = models.IntegerField()
    tipo_compra = models.BooleanField()

    usuario = models.ForeignKey(Usuarios, null=True, on_delete=models.CASCADE)


class Rel_Prod_Comp(models.Model):
    cantidad_comprada = models.IntegerField()
    compra = models.ForeignKey(Compras, on_delete=models.CASCADE)
