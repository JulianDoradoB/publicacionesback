from django.db import models

class Publicacion(models.Model):
    contenido = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(max_length=50)

