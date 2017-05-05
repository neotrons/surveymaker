# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-05 11:32
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formbuilds', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='block',
            old_name='legend',
            new_name='title',
        ),
        migrations.AddField(
            model_name='block',
            name='form',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='formbuilds.Form'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='block',
            name='help_text',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Texto de ayuda'),
        ),
        migrations.AddField(
            model_name='field',
            name='fieldset',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='formbuilds.Fieldset'),
        ),
        migrations.AddField(
            model_name='fieldset',
            name='show',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='field',
            name='form',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='formbuilds.Form'),
        ),
        migrations.AlterField(
            model_name='field',
            name='type',
            field=models.CharField(choices=[('1', 'Texto'), ('2', 'Verdadero o Falso'), ('3', 'Radio'), ('4', 'Seleccion multiple'), ('5', 'Seleccion'), ('6', 'Cargar documento'), ('7', 'Textarea'), ('8', 'A\xf1o-Mes-D\xeda'), ('9', 'Recortar Imagen'), ('14', 'Ubigeo:Pais'), ('10', 'Ubigeo:Departamento'), ('11', 'Ubigeo:Provincia'), ('12', 'Ubigeo:Distrito'), ('13', 'e-mail')], default=('1', 'Texto'), max_length=2),
        ),
    ]
