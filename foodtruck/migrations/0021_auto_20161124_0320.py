# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-24 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0020_auto_20161124_0319'),
    ]

    operations = [
        migrations.AddField(
            model_name='foodtruck',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='foodtruck',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
