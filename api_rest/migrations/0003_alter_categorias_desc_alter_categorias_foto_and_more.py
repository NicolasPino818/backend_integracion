# Generated by Django 4.2 on 2023-05-10 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0002_alter_data_usd_clp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categorias',
            name='desc',
            field=models.CharField(max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name='categorias',
            name='foto',
            field=models.BinaryField(null=True),
        ),
        migrations.AlterField(
            model_name='marcas',
            name='pais',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
