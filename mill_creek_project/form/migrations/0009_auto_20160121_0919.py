# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0008_auto_20160121_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='company_name',
            field=models.TextField(default='Test', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.TextField(default='Test', max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='website',
            field=models.TextField(default='Test', max_length=200),
        ),
    ]
