# Generated by Django 4.0.3 on 2022-03-26 21:19

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('videoclub', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='empleado',
            name='apellido',
        ),
        migrations.AddField(
            model_name='empleado',
            name='apellidos',
            field=models.CharField(default='default', max_length=60),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellidos',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='idCliente',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='idEmpleado',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='empleado',
            name='nombre',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='genero',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='idPelicula',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='pelicula',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='videoclub',
            name='idVideoclub',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='videoclub',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
        migrations.CreateModel(
            name='Alquilado',
            fields=[
                ('idAlquiler', models.AutoField(primary_key=True, serialize=False)),
                ('fecha_de_alquiler', models.DateField(default=datetime.date.today)),
                ('idCliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='videoclub.cliente')),
                ('idEmpleado', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='videoclub.empleado')),
                ('idPelicula', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='videoclub.pelicula')),
                ('idVideoclub', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='videoclub.videoclub')),
            ],
        ),
    ]
