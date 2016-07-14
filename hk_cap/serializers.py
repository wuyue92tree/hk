#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .models import Http
from rest_framework import serializers


class HttpSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Http
        fields = ('id', 'sip', 'dip', 'sport', 'dport', 'method', 'platform', 'browser', 'cookie', 'host', 'uri', 'url')

