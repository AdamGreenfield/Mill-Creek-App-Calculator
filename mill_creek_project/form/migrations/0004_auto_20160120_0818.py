# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-20 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0003_auto_20160119_0926'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='text',
            new_name='comments',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='title',
            new_name='company_name',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.AddField(
            model_name='post',
            name='email',
            field=models.CharField(default='Test', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='name',
            field=models.CharField(default='Test', max_length=200),
        ),
        migrations.AddField(
            model_name='post',
            name='website',
            field=models.CharField(default='Test', max_length=200),
        ),
    ]