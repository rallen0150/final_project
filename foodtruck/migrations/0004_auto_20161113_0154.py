# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-13 01:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0003_commenter_favorite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commenter',
            name='favorite',
            field=models.ManyToManyField(blank=True, null=True, to='foodtruck.Foodtruck'),
        ),
    ]
