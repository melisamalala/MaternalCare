# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-04 20:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mama', '0016_auto_20181104_2322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctorworkinghours',
            name='doctor',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='working_hours', to='mama.Doctor'),
        ),
    ]
