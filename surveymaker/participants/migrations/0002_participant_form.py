# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-05 14:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('formbuilds', '0006_upload'),
        ('participants', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='form',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='formbuilds.Form'),
            preserve_default=False,
        ),
    ]
