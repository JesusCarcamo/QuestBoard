from django.db import models


# Create your models here.
class Jugador(models.Model):

    nombre = models.CharField(max_length=100)
    apodo = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    edad = models.IntegerField()
    avatar = models.CharField(max_length=400)
    pais = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    ciudad = models.CharField(max_length=100)
    # ----------------Relaciones-------------------
    recompensas = models.ManyToManyField('Recompensa', through='JugadorRecompensa')
    juegos=models.ManyToManyField('Juego', through='JugadorJuego')
    #amigos=models.ManyToManyField('self', default= None,null=True)
    #notificaciones = models.ManyToManyField('Notificacion', default= None,null=True)


class Mision(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    vigencia = models.DateField()
    minJugadores = models.IntegerField(default=1)
    maxJugadores = models.IntegerField(default=1)
    completada = models.BooleanField(default=False)
    #----------------Relaciones-------------------
    contratista = models.ForeignKey(Jugador, on_delete=models.DO_NOTHING)
    cazaRecompensas = models.ManyToManyField(Jugador, default=None, null=True, related_name='misionesAdquiridas')
    recompensas=models.ManyToManyField('Recompensa', through='MisionRecompensa')
    juego= models.ForeignKey('Juego', related_name='misiones', on_delete=models.DO_NOTHING)
    logro = models.ForeignKey('Logro', null=True, related_name="misiones", on_delete=models.DO_NOTHING)


class Recompensa(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=100)
    tipo = models.CharField(max_length=100)
    imagen = models.CharField(max_length=400)


class MisionRecompensa(models.Model):
    cantidad = models.PositiveIntegerField()
    mision = models.ForeignKey(Mision, on_delete=models.DO_NOTHING)
    recompensa = models.ForeignKey(Recompensa, on_delete=models.DO_NOTHING)


class JugadorRecompensa(models.Model):
    cantidad = models.PositiveIntegerField()
    jugador = models.ForeignKey(Jugador, on_delete=models.DO_NOTHING)
    recompensa = models.ForeignKey(Recompensa, on_delete=models.DO_NOTHING)


class Juego(models.Model):
    nombre = models.CharField(max_length=100)
    genero = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=1000)


class Logro(models.Model):
    imagen = models.CharField(max_length=400)
    nombre = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=400)
    # ----------------Relaciones-------------------
    juego=models.ForeignKey(Juego, related_name='logros', on_delete=models.DO_NOTHING)


class Dia(models.Model):
    NombreDia = (
        ('L', 'Lunes'),
        ('M', 'Martes'),
        ('I', 'Miercoles'),
        ('J', 'Jueves'),
        ('V', 'Viernes'),
        ('S', 'Sabado'),
        ('D', 'Domingo'),
    )
    nombre = models.CharField(max_length=1, choices=NombreDia)
    intervalo = models.CharField(max_length=100)
    # ----------------Relaciones-------------------
    jugador = models.ForeignKey(Jugador, null=True, related_name='horarioJuego', on_delete=models.DO_NOTHING)
    jugador_juego = models.ForeignKey('JugadorJuego', null=True, related_name='horarioJuego',
                                      on_delete=models.DO_NOTHING)


class JugadorJuego(models.Model):
    horasJugadas=models.PositiveIntegerField()
    estadisticas= models.TextField(null= True, blank=True)
    logros = models.ManyToManyField(Logro, through='JugadorJuegoLogro')
    jugador = models.ForeignKey(Jugador, on_delete=models.DO_NOTHING)
    juego = models.ForeignKey(Juego, on_delete=models.DO_NOTHING)


class JugadorJuegoLogro(models.Model):
    completado = models.BooleanField()
    jugadorJuego = models.ForeignKey(JugadorJuego, on_delete=models.DO_NOTHING)
    logro = models.ForeignKey(Logro, on_delete=models.DO_NOTHING)


class Mensaje(models.Model):
    contenido = models.TextField()
    jugador_from = models.ForeignKey(Jugador, related_name='mensajes_enviados', on_delete=models.DO_NOTHING)
    jugador_to = models.ForeignKey(Jugador, related_name='mensajes_recibidos', on_delete=models.DO_NOTHING)


class SolicitudAmistad(models.Model):
    aceptada = models.BooleanField(default=False)
    jugador_from = models.ForeignKey(Jugador, related_name='solicitudesAmistad_enviadas', on_delete=models.DO_NOTHING)
    jugador_to = models.ForeignKey(Jugador, related_name='solicitudesAmistad_recibidas', on_delete=models.DO_NOTHING)


class Notificacion(models.Model):
    tipoAviso = models.CharField(max_length=100)
    mensaje = models.CharField(max_length=100)


#######################################################333333
# class Equipo(models.Model):
#
#     nombre = models.CharField(max_length=100)
#     logo = models.CharField(max_length=400)
#
# class TorneoRecompensa(models.Model):
#
#     cantidad = models.IntegerField(default=0)
#     recompensaPosicion= models.IntegerField(default=0)
#
# class Torneo(models.Model):
#
#     fechaInicio = models.DateField(auto_now=False, auto_now_add=False)
#     fechaFin = models.DateField(auto_now=False, auto_now_add=False)
#     maxEquipos = models.IntegerField(default=0)
#     minEquipos = models.IntegerField(default=0)
#     terminado = models.BooleanField(default=False)
#
# class Empresa(models.Model):
#
#     nombre = models.CharField(max_length=100)


