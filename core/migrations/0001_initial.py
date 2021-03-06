# Generated by Django 3.2.3 on 2021-06-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('rut', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('razonSocial', models.CharField(max_length=50)),
                ('descripcion', models.TextField(max_length=100)),
                ('telefono', models.CharField(max_length=15)),
                ('email', models.CharField(max_length=100)),
                ('tipoServicio', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('codigoIdentificador', models.CharField(max_length=15, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
