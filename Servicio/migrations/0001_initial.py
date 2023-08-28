# Generated by Django 4.2 on 2023-04-29 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titulo', models.CharField(max_length=50)),
                ('Contenido', models.CharField(max_length=50)),
                ('Imagen', models.ImageField(upload_to='')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Update', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
            },
        ),
    ]
