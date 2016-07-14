# -*- coding: utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Http(models.Model):
    id = models.IntegerField(primary_key=True)
    sip = models.CharField(max_length=20, blank=True, null=True)
    dip = models.CharField(max_length=20, blank=True, null=True)
    sport = models.CharField(max_length=20, blank=True, null=True)
    dport = models.CharField(max_length=20, blank=True, null=True)
    method = models.CharField(max_length=20, blank=True, null=True)
    platform = models.CharField(max_length=20, blank=True, null=True)
    browser = models.CharField(max_length=20, blank=True, null=True)
    cookie = models.CharField(max_length=1000, blank=True, null=True)
    host = models.CharField(max_length=100, blank=True, null=True)
    uri = models.CharField(max_length=1000, blank=True, null=True)
    url = models.URLField(max_length=1000, blank=True, null=True)
    url_type = models.CharField(max_length=20, blank=True, null=True)
    time = models.DateTimeField(blank=True, null=True)

    class Meta:
        # managed = False
        db_table = 'http'
        verbose_name = "HTTP数据"
        verbose_name_plural = verbose_name
