# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-30 10:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accountuser',
            name='is_staff',
            field=models.BooleanField(default=False, verbose_name=b'staff'),
        ),
    ]
