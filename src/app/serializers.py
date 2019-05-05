from rest_framework import serializers
from .models import Jugador, Mision, Juego, Dia

class JugadorSerializer (serializers.Serializer):
    
    nombre = serializers.CharField(required=True, allow_blank=False, max_length=100)
    apodo = serializers.CharField(required=True, allow_blank=False, max_length=100)
    email = serializers.CharField(required=True, allow_blank=False, max_length=100)
    password = serializers.CharField(required=True, allow_blank=False, max_length=100)
    edad = serializers.IntegerField()
    avatar = serializers.CharField(required=True, allow_blank=False, max_length=400)
    pais = serializers.CharField(required=True, allow_blank=False, max_length=100)
    estado = serializers.CharField(required=True, allow_blank=False, max_length=400)
    ciudad = serializers.CharField(required=True, allow_blank=False, max_length=100)
    mensajes = serializers.StringRelatedField(many=True)
    notificaciones = serializers.StringRelatedField(many=True)
    amigos = serializers.StringRelatedField(many=True)
    solicitudesAmistad = serializers.StringRelatedField(many=True)
    misiones = serializers.StringRelatedField(many=True)
    recompensas = serializers.StringRelatedField(many=True)
    juegos = serializers.StringRelatedField(many=True)
	horarioJuego = serializers.StringRelatedField(many=True)
	equipos = serializers.StringRelatedField(many=True)	
    
    def create(self, validated_data):
        return Jugador.objects.create(**validated_data)

class MisionSerializer (serializers.Serializer):
    
    nombre = serializers.CharField(required=True, allow_blank=False, max_length=100)
    descripcion = serializers.CharField(required=True, allow_blank=False, max_length=100)
    vigencia = serializers.DateField()
    minJugadores = serializers.IntegerField(required=True)
    maxJugadores = serializers.IntegerField(required=True)
    aceptada = serializers.BooleanField(required=True)
    contratista = serializers.StringRelatedField(many=False)
    cazaRecompensas = serializers.StringRelatedField(many=True)
	logro = serializers.StringRelatedField(many=False)
	recompensas = serializers.StringRelatedField(many=True)
	juego = serializers.StringRelatedField(many=False)
	empresa = serializers.StringRelatedField(many=False)
	
    def create(self, validated_data):
        return Mision.objects.create(**validated_data)
    
class JuegoSerializer (serializers.Serializer):
    
    nombre = serializers.CharField(required=True, allow_blank=False, max_length=100)
    genero = serializers.CharField(required=True, allow_blank=False,max_length=100)
    descripcion = serializers.CharField(required=True, allow_blank=False,max_length=100)
    jugador = serializers.StringRelatedField(many=False)
    horasJugadas = serializers.CharField(required=True, allow_blank=False,max_length=100)
    estadisticas = serializers.CharField(required=True, allow_blank=False,max_length=600)
    dia = serializers.StringRelatedField(many=False, required=False)
	misiones = serializers.StringRelatedField(many=True)
	logros = serializers.StringRelatedField(many=True)
    
    def create(self, validated_data):
        return Mision.objects.create(**validated_data)
    
class DiaSerializer (serializers.Serializer):
    
    nombre = serializers.CharField(required=True, allow_blank=False, max_length=100)
    intervalo = serializers.CharField(required=True, allow_blank=False, max_length=100)
    jugador = serializers.StringRelatedField(many=True, required=False)
    
    def create(self, validated_data):
        return Dia.objects.create(**validated_data)

class MensajeSerializer (serializers.Serializer):
    
    contenido = serializers.CharField(required=True, allow_blank=False, max_length=100)
	de = serializers.StringRelatedField(many=False)
	para = serializers.StringRelatedField(many=False)
	
    def create(self, validated_data):
        return Mensaje.objects.create(**validated_data)
		
class NotificacionSerializer (serializers.Serializer):
    
    tipoAviso = serializers.CharField(required=True, allow_blank=False, max_length=100)
    mensaje = serializers.CharField(required=True, allow_blank=False, max_length=100)
	
    def create(self, validated_data):
        return Notificacion.objects.create(**validated_data)
		
class RecompensaSerializer (serializers.Serializer):
    
    nombre = serializers.CharField(required=True, allow_blank=False, max_length=100)
    descripcion = serializers.CharField(required=True, allow_blank=False, max_length=100)
    tipo = serializers.CharField(required=True, allow_blank=False, max_length=100)
	
    def create(self, validated_data):
        return Recompensa.objects.create(**validated_data)

class SolicitudAmistadSerializer (serializers.Serializer):
    
    contenido = serializers.BooleanField(required=True)
	de = serializers.StringRelatedField(many=False)
	para = serializers.StringRelatedField(many=False)
	
    def create(self, validated_data):
        return SolicitudAmistad.objects.create(**validated_data)
		
class EquipoSerializer (serializers.Serializer):
    
    nombre = serializers.CharField(required=True, allow_blank=False, max_length=100)
    logo = serializers.CharField(required=True, allow_blank=False, max_length=400)
	jugadores = serializers.StringRelatedField(many=True)	
	torneos = serializers.StringRelatedField(many=True)
	juego = serializers.StringRelatedField(many=False)
	
    def create(self, validated_data):
        return Equipo.objects.create(**validated_data)

class MisionRecompensaSerializer (serializers.Serializer):
    
    contenido = serializers.IntegerField()
	mision = serializers.StringRelatedField(many=False)
	recompensa = serializers.StringRelatedField(many=False)
	
    def create(self, validated_data):
        return MisionRecompensa.objects.create(**validated_data)
		
class TorneoRecompensaSerializer (serializers.Serializer):
    
    cantidad = serializers.IntegerField()
    recompensaPosicion = serializers.IntegerField()
	recompensa = serializers.StringRelatedField(many=False)
	torneo = serializers.StringRelatedField(many=False)
	
    def create(self, validated_data):
        return TorneoRecompensa.objects.create(**validated_data)		
		
class UsuarioRecompensaSerializer (serializers.Serializer):
    
    cantidad = serializers.IntegerField()
	jugador = serializers.StringRelatedField(many=False)
	recompensa = serializers.StringRelatedField(many=False)
	
    def create(self, validated_data):
        return UsuarioRecompensa.objects.create(**validated_data)

class TorneoSerializer (serializers.Serializer):
    
    fechaInicio = serializers.DateField()
	fechaFin = serializers.DateField()
    maxEquipos = serializers.IntegerField(required=True)
    minEquipos = serializers.IntegerField(required=True)
    terminado = serializers.BooleanField(required=True)
	recompensas = serializers.StringRelatedField(many=True)
	equipos = serializers.StringRelatedField(many=True)
	juego = serializers.StringRelatedField(many=False) 
	
    def create(self, validated_data):
        return Torneo.objects.create(**validated_data)

class EmpresaSerializer (serializers.Serializer):
    
    nombre = serializers.CharField(required=True, allow_blank=False, max_length=100)
	juegos = serializers.StringRelatedField(many=True)
	
    def create(self, validated_data):
        return Empresa.objects.create(**validated_data)		

class LogroSerializer (serializers.Serializer):
    
    nombre = serializers.CharField(required=True, allow_blank=False, max_length=100)
    descripcion = serializers.CharField(required=True, allow_blank=False, max_length=100)
    imagen = serializers.CharField(required=True, allow_blank=False, max_length=400)
	juego = serializers.StringRelatedField(many=False)
	
    def create(self, validated_data):
        return Recompensa.objects.create(**validated_data)
		
class UsuarioJuegoLogroSerializer (serializers.Serializer):
    
    completado = serializers.BooleanField(required=True)
	usuario_juego = serializers.StringRelatedField(many=False)
	logro = serializers.StringRelatedField(many=False)
	
    def create(self, validated_data):
        return UsuarioJuegoLogro.objects.create(**validated_data)

class UsuarioJuegoSerializer (serializers.Serializer):
    
    horasJugadas = serializers.CharField(required=True, allow_blank=False, max_length=100)
    estadisticas = serializers.CharField(required=True, allow_blank=False, max_length=600)
	usuario = serializers.StringRelatedField(many=False)
	juego = serializers.StringRelatedField(many=False)
	horarioJuego = serializers.StringRelatedField(many=True)
	logros = serializers.StringRelatedField(many=True)
	
    def create(self, validated_data):
        return UsuarioJuego.objects.create(**validated_data)			