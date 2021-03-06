# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-19 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0030_auto_20160218_0957'),
    ]

    operations = [
        migrations.CreateModel(
            name='Costs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Costs', editable=False, max_length=10)),
                ('iOSCost', models.IntegerField(default=0)),
                ('androidCost', models.IntegerField(default=0)),
                ('loginCost', models.IntegerField(default=0)),
                ('emailLoginCost', models.IntegerField(default=0)),
                ('socialLoginCost', models.IntegerField(default=0)),
                ('upfrontCost', models.IntegerField(default=0)),
                ('inappCost', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Cost',
                'verbose_name_plural': 'Costs',
            },
        ),
        migrations.DeleteModel(
            name='androidCost',
        ),
        migrations.DeleteModel(
            name='emailLoginCost',
        ),
        migrations.DeleteModel(
            name='inappCost',
        ),
        migrations.DeleteModel(
            name='iOSCost',
        ),
        migrations.DeleteModel(
            name='loginCost',
        ),
        migrations.DeleteModel(
            name='socialLoginCost',
        ),
        migrations.DeleteModel(
            name='upfrontCost',
        ),
    ]
