# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 15:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0009_auto_20160121_0919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='company_name',
            field=models.CharField(default='Test', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.CharField(default='Test', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(default='Test', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='website',
            field=models.CharField(default='Test', max_length=200),
        ),
    ]
