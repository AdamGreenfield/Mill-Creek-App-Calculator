# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-22 15:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0010_auto_20160121_0920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='published_date',
        ),
        migrations.AlterField(
            model_name='post',
            name='comments',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='post',
            name='company_name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='email',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='post',
            name='website',
            field=models.CharField(max_length=200),
        ),
    ]
