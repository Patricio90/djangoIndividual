# Generated by Django 4.0.5 on 2022-06-15 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='correo',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AddField(
            model_name='cliente',
            name='edad',
            field=models.IntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='apellido',
            field=models.CharField(default=None, max_length=100),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(default=None, max_length=50),
        ),
    ]
