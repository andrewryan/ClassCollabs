# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-09 04:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectApps', '0002_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='result',
            old_name='username',
            new_name='users',
        ),
    ]
