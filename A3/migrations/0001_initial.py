# Generated by Django 2.2.4 on 2019-08-13 16:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PuntosFijos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=300, null=True)),
                ('numero_de_chaleco', models.CharField(blank=True, max_length=10, null=True)),
                ('direccion', models.CharField(blank=True, max_length=300, null=True)),
                ('hora_de_ingreso', models.CharField(blank=True, max_length=300, null=True)),
                ('hora_de_salida', models.CharField(blank=True, max_length=300, null=True)),
                ('noverdad', models.CharField(blank=True, max_length=300, null=True)),
                ('fecha_de_creacion', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
