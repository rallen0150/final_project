# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-07-30 19:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0024_auto_20161129_1853'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodtruck',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='foodtruck',
            name='start_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
