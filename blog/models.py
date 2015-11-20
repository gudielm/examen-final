from django.db import models
from django.utils import timezone

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.CharField(max_length=10)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.usuario

class Comentario(models.Model):
    usuario = models.ForeignKey('Usuario')
    producto = models.ForeignKey('Producto')
    opinion = models.TextField()
    published_date = models.DateTimeField(
                blank=True, null=True)
    puntuacion = models.CharField(max_length=5)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.puntuacion

# Create your models here  ...('auth.User')
