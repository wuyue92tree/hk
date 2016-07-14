from django.shortcuts import render

# Create your views here.
from django.contrib.auth.models import Group
from .models import Http
from rest_framework import viewsets
from .serializers import HttpSerializer


class HttpViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Http.objects.all().order_by('-time')
    serializer_class = HttpSerializer

