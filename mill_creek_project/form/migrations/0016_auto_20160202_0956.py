# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-02 15:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0015_auto_20160202_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='login',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=200),
        ),
    ]