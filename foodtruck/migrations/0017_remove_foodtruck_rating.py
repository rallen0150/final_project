# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-22 16:54
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodtruck', '0016_profile_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foodtruck',
            name='rating',
        ),
    ]
