# Generated by Django 4.2 on 2023-04-30 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Servicio', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='servicio',
            name='Imagen',
            field=models.ImageField(upload_to='Proyectoweb/media/servicio'),
        ),
    ]
