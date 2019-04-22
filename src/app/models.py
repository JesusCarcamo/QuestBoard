from conda_build.os_utils.pyldd import machofile
from django.db import models


# Create your models here.
class Jugador(models.Model):

    nombre = models.CharField(max_length=100)
    apodo = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    edad = models.IntegerField(default=0)
    avatar = models.CharField(max_length=400)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=400)
    ciudad = models.CharField(max_length=100)


class Mensaje(models.Model):

    contenido = models.CharField(max_length=400)


class Notificacion(models.Model):

    tipoAviso = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=100)


class Recompensa(models.Model):

    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)


class SolicitudAmistad(models.Model):

    aceptada = models.BooleanField(default=False)


class Equipo(models.Model):

    nombre = models.CharField(max_length=100)
    logo = models.CharField(max_length=400)


class MisionRecompensa(models.Model):

    cantidad = models.IntegerField(default=0)


class TorneoRecompensa(models.Model):

    cantidad = models.IntegerField(default=0)
    recompensaPosicion= models.IntegerField(default=0)


class UsuarioRecompensa(models.Model):

    cantidad = models.IntegerField(default=0)




