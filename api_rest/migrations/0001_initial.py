# Generated by Django 4.2.1 on 2023-05-03 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categorias',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_categoria', models.CharField(max_length=200)),
                ('foto', models.BinaryField()),
                ('desc', models.CharField(max_length=2500)),
            ],
        ),
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_compra', models.DateField()),
                ('total', models.IntegerField()),
                ('tipo_compra', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usd_clp', models.IntegerField()),
                ('fecha_actualizacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Marcas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_marca', models.CharField(max_length=150)),
                ('pais', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='Personas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=250)),
                ('apellidos', models.CharField(max_length=250, null=True)),
                ('rut', models.CharField(max_length=20, null=True, unique=True)),
                ('tel', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_producto', models.CharField(max_length=200)),
                ('precio', models.IntegerField()),
                ('precio_ofer', models.IntegerField(null=True)),
                ('imagen', models.BinaryField(null=True)),
                ('stock', models.IntegerField()),
                ('fecha_creacion', models.DateField()),
                ('desc', models.CharField(max_length=2500)),
                ('color', models.CharField(max_length=150, null=True)),
                ('trastes', models.CharField(max_length=150, null=True)),
                ('mat_cuerpo', models.CharField(max_length=150, null=True)),
                ('mat_neck', models.CharField(max_length=150, null=True)),
                ('mat_fingerb', models.CharField(max_length=150, null=True)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.categorias')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.marcas')),
            ],
        ),
        migrations.CreateModel(
            name='Roles',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_rol', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.CharField(max_length=80, unique=True)),
                ('correo', models.CharField(max_length=200, unique=True)),
                ('passw', models.CharField(max_length=255)),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.personas', unique=True)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.roles', unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Rel_Prod_Comp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('compra', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.compras', unique=True)),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api_rest.productos')),
            ],
        ),
        migrations.AddField(
            model_name='compras',
            name='usuario',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api_rest.usuarios'),
        ),
    ]
