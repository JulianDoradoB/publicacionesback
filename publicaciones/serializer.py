from rest_framework import serializers
from .models import Publicacion

class PublicacionSerializer(serializers.ModelSerializer):
    class Meta:
        model=Publicacion
        fields = ['id', 'contenido', 'fecha', 'tipo']
