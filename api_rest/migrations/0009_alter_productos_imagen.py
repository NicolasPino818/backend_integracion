# Generated by Django 4.2.1 on 2023-05-16 15:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api_rest', '0008_alter_productos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.TextField(blank=True, null=True),
        ),
    ]
