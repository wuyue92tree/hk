# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-15 02:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20160530_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountuser',
            name='first_name',
            field=models.CharField(blank=True, max_length=100, verbose_name=b'\xe5\x90\x8d'),
        ),
        migrations.AlterField(
            model_name='accountuser',
            name='last_name',
            field=models.CharField(max_length=100, unique=True, verbose_name=b'\xe5\xa7\x93'),
        ),
    ]