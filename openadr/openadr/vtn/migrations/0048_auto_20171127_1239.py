# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-27 20:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vtn', '0047_auto_20171122_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='telemetry',
            name='actual_kW',
        ),
        migrations.RemoveField(
            model_name='telemetry',
            name='baseline_energy_kwh',
        ),
        migrations.RemoveField(
            model_name='telemetry',
            name='baseline_kW',
        ),
        migrations.RemoveField(
            model_name='telemetry',
            name='energy_kwh',
        ),
        migrations.RemoveField(
            model_name='telemetry',
            name='measured_energy_kwh',
        ),
        migrations.RemoveField(
            model_name='telemetry',
            name='shed_kW',
        ),
    ]
