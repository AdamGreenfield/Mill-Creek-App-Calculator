# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('form', '0024_delete_post'),
    ]

    operations = [
        migrations.CreateModel(
            name='Costs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Costs', editable=False, max_length=10)),
                ('platformCost', models.IntegerField()),
                ('loginCost', models.IntegerField()),
            ],
        ),
    ]