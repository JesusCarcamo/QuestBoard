from rest_framework import serializers
from .models import *


#------------------------Clases de asociacion--------------------------------
class MisionRecompensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MisionRecompensa
        fields = '__all__'


class JugadorRecompensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = JugadorRecompensa
        fields = '__all__'


class JugadorJuegoLogroSerializer(serializers.ModelSerializer):
    class Meta:
        model = JugadorJuegoLogro
        fields = '__all__'


class DiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dia
        fields = '__all__'


class JugadorJuegoSerializer(serializers.ModelSerializer):
    horarioJuego=DiaSerializer(read_only=True, many=True)
    class Meta:
        model = JugadorJuego
        fields = '__all__'


#--------------------------Clases normales----------------------------------
class SolicitudAmistadSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolicitudAmistad
        fields = '__all__'


class MensajeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mensaje
        fields = '__all__'


class JugadorSerializer(serializers.ModelSerializer):
    solicitudesAmistad_enviadas= SolicitudAmistadSerializer(read_only=True, many=True)
    solicitudesAmistad_recibidas = SolicitudAmistadSerializer(read_only=True, many=True)
    mensajes_enviados= MensajeSerializer(read_only=True, many=True)
    mensajes_recibidos = MensajeSerializer(read_only=True, many=True)
    horarioJuego= DiaSerializer(read_only=True, many=True)
    class Meta:
        model = Jugador
        fields = '__all__'


class MisionSerializer(serializers.ModelSerializer):
    cazaRecompensas = JugadorSerializer(read_only=True, many=True)
    class Meta:
        model = Mision
        fields = '__all__'


class RecompensaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recompensa
        fields = '__all__'


class LogroSerializer(serializers.ModelSerializer):
    misiones = MisionSerializer(read_only=True, many=True)
    class Meta:
        model = Logro
        fields = '__all__'


class JuegoSerializer(serializers.ModelSerializer):
    misiones = MisionSerializer(read_only=True, many=True)
    logros = LogroSerializer(read_only=True, many=True)
    class Meta:
        model = Juego
        fields = '__all__'


class NotificacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notificacion
        fields = '__all__'


class LeagueSerializer(serializers.ModelSerializer):
    class Meta:
        model = League
        fields = '__all__'



