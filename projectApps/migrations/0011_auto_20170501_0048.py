# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-01 00:48
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projectApps', '0010_chat'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chat',
            name='user',
        ),
        migrations.DeleteModel(
            name='Chat',
        ),
    ]
