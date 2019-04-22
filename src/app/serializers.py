from rest_framework import serializers
from .models import Jugador, Mision, Juego, Dia

class JugadorSerializer (serializers.Serializers):
    
    nombre = serializers.CharField(required=True, allow_blank=False, max_length=100)
    apodo = serializers.CharField(required=True, allow_blank=False, max_length=100)
    email = serializers.CharField(required=True, allow_blank=False, max_length=100)
    password = serializers.CharField(required=True, allow_blank=False, max_length=100)
    edad = serializers.IntegerField()
    avatar = serializers.CharField(required=True, allow_blank=False, max_length=400)
    pais = serializers.CharField(required=True, allow_blank=False, max_length=100)
    estado = serializers.CharField(required=True, allow_blank=False, max_length=400)
    ciudad = serializers.CharField(required=True, allow_blank=False, max_length=100)
    
    def create(self, validated_data):
        return Jugador.objects.create(**validated_data)

class MisionSerializer (serializers.Serializers):
    
    nombre = serializers.CharField(required=True, allow_blank=False, max_length=100)
    descripcion = serializers.CharField(required=True, allow_blank=False, max_length=100)
    vigencia = serializers.DateField()
    minJugadores = serializers.IntegerField(required=True, allow_blank=False, default=0)
    maxJugadores = serializers.IntegerField(required=True, allow_blank=False, default=0)
    aceptada = serializers.BooleanField(required=True, allow_blank=False, default=False)
    jugador = serializers.StringRelatedField(many=False, required=True)
    
    def create(self, validated_data):
        return Mision.objects.create(**validated_data)
    
class JuegoSerializer (serializers.Serializers):
    
    nombre = serializers.CharField(required=True, allow_blank=False, max_length=100)
    genero = serializers.CharField(required=True, allow_blank=False,max_length=100)
    descripcion = serializers.CharField(required=True, allow_blank=False,max_length=100)
    jugador = serializers.StringRelatedField(many=False, required=True)
    horasJugadas = serializers.CharField(required=True, allow_blank=False,max_length=100)
    estadisticas = serializers.CharField(required=True, allow_blank=False,max_length=600)
    dia = serializers.StringRelatedField(many=False, required=False)
    
    def create(self, validated_data):
        return Mision.objects.create(**validated_data)
    
class DiaSerializer (serializers.Serializers):
    
    nombre = serializers.CharField(required=True, allow_blank=False, max_length=100)
    intervalo = serializers.CharField(required=True, allow_blank=False, max_length=100)
    jugador = serializers.StringRelatedField(many=True, required=False)