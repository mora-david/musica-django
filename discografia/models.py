Sfrom django.db import models


# Create your models here.
class Discografia(models.Model):
    nombre = models.CharField(max_length=200)
    artista = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre
