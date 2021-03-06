# Generated by Django 4.0.3 on 2022-03-15 10:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('idCliente', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('apellidos', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Videoclub',
            fields=[
                ('idVideoclub', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('idPelicula', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('genero', models.TextField()),
                ('duracion', models.IntegerField()),
                ('fecha_de_lanzamiento', models.DateField(default=datetime.date.today)),
                ('idVideoclub', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='videoclub.videoclub')),
            ],
        ),
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idEmpleado', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.TextField()),
                ('apellido', models.TextField()),
                ('idVideoclub', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='videoclub.videoclub')),
            ],
        ),
    ]
