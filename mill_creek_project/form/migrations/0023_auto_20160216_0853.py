# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-16 14:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0022_auto_20160216_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='androidCost',
        ),
        migrations.RemoveField(
            model_name='post',
            name='iOSCost',
        ),
        migrations.RemoveField(
            model_name='post',
            name='loginCost',
        ),
    ]
