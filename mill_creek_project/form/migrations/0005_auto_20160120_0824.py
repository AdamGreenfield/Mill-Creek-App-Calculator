# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 14:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0004_auto_20160120_0818'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='comments',
        ),
        migrations.RemoveField(
            model_name='post',
            name='company_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='created_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='email',
        ),
        migrations.RemoveField(
            model_name='post',
            name='name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.RemoveField(
            model_name='post',
            name='website',
        ),
    ]
