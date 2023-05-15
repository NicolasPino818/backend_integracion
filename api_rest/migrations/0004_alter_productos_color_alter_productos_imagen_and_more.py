# Generated by Django 4.2 on 2023-05-14 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0003_alter_categorias_desc_alter_categorias_foto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='color',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.BinaryField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='mat_cuerpo',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='mat_fingerb',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='mat_neck',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='precio_ofer',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productos',
            name='trastes',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]