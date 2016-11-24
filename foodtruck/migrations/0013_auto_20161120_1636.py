# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-20 16:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0012_remove_foodtruck_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='foodtruck',
            old_name='driver',
            new_name='user',
        ),
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(choices=[('T', 'Truck useruser'), ('A', 'User Account')], max_length=1),
        ),
    ]