from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PublicacionSerializer
from .models import Publicacion

class PublicacionViewSet(viewsets.ModelViewSet):
    queryset= Publicacion.objects.all()
    serializer_class = PublicacionSerializer