# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 14:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0025_costs'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Costs',
            new_name='Cost',
        ),
    ]
