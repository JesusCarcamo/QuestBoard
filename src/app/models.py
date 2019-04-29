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
    
class Dia(models.Model):
    
    nombre = models.CharField(max_length=100)
    intervalo = models.CharField(max_length=100)
    jugador = models.ForeignKey(Jugador, on_delete=models.DO_NOTHING)


class Mision(models.Model):
    
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    vigencia = models.DateField(auto_now=False, auto_now_add=False)
    minJugadores = models.IntegerField(default=0)
    maxJugadores = models.IntegerField(default=0)
    aceptada = models.BooleanField(default=False)
    jugador = models.ForeignKey(Jugador, on_delete=models.CASCADE)


class Torneo(models.Model):
    
    fechaInicio = models.DateField(auto_now=False, auto_now_add=False)
    fechaFin = models.DateField(auto_now=False, auto_now_add=False)
    maxEquipos = models.IntegerField(default=0)
    minEquipos = models.IntegerField(default=0)
    terminado = models.BooleanField(default=False)


class Juego(models.Model):
    
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    jugador = models.ForeignKey(Jugador, on_delete=models.DO_NOTHING)
    horasJugadas = models.CharField(max_length=100)
    estadisticas = models.CharField(max_length=600)
    dia = models.ForeignKey(Dia, on_delete=models.DO_NOTHING)


class Empresa(models.Model):
    
    nombre = models.CharField(max_length=100)


class Logro(models.Model):
    
    imagen = models.CharField(max_length=400)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)


class UsuarioJuegoLogro(models.Model):
    
    aceptada = models.BooleanField(default=False)

