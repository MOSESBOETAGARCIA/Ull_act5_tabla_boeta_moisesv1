from django.db import models

# Create your models here.
class cliente(models.Model):
    
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    telefono = models.CharField(max_length=100)
    
    def __srt__(self):
        return f"{self.nombre} {self.apellido}"
    