# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-11-04 19:21
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mama', '0009_auto_20181103_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorWorkingHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('working_from', models.CharField(choices=[(6, '6:00 am'), (7, '7:00 am'), (8, '8:00 am'), (9, '9:00 am'), (10, '10:00 am'), (11, '11:00 am'), (12, '12:00 am'), (13, '1: 00 pm'), (14, '2: 00 pm'), (15, '3: 00 pm'), (16, '4: 00 pm'), (17, '5: 00 pm'), (18, '6: 00 pm')], max_length=1)),
                ('working_to', models.CharField(choices=[(6, '6:00 am'), (7, '7:00 am'), (8, '8:00 am'), (9, '9:00 am'), (10, '10:00 am'), (11, '11:00 am'), (12, '12:00 am'), (13, '1: 00 pm'), (14, '2: 00 pm'), (15, '3: 00 pm'), (16, '4: 00 pm'), (17, '5: 00 pm'), (18, '6: 00 pm')], max_length=1)),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='working_hours', to='mama.Doctor')),
            ],
        ),
        migrations.RemoveField(
            model_name='doctorschedule',
            name='doctor',
        ),
        migrations.RenameField(
            model_name='appointment',
            old_name='booked',
            new_name='is_booked',
        ),
        migrations.AddField(
            model_name='appointment',
            name='day',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2018, 11, 4, 22, 21, 16, 801687)),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='DoctorSchedule',
        ),
    ]