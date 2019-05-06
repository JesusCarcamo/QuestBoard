import requests
import json
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect

from rest_framework import generics
from rest_framework.parsers import JSONParser
from .models import *
from .serializers import *

# Create your views here.
def inicio(request):
    return render(request, "base.html")


class JuegoC(dict):
    def __init__(self, nivel, nombreInvocador, region, maestriaTotal):
        dict.__init__(self, nombre='League of Legends', genero='MOBA', descripcion='Juegazo', nivel=nivel, nombreInvocador=nombreInvocador, region=region, maestriaTotal=maestriaTotal)



#-------------------------------Clases de Asociacion--------------------------------------------------------------------


class MisionRecompensaList(generics.ListCreateAPIView):
    queryset = MisionRecompensa.objects.all()
    serializer_class = MisionRecompensaSerializer


class MisionRecompensaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MisionRecompensa.objects.all()
    serializer_class = MisionRecompensaSerializer


class JugadorRecompensaList(generics.ListCreateAPIView):
    queryset = JugadorRecompensa.objects.all()
    serializer_class = JugadorRecompensaSerializer


class JugadorRecompensaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JugadorRecompensa.objects.all()
    serializer_class = JugadorRecompensaSerializer


class JugadorJuegoLogroList(generics.ListCreateAPIView):
    queryset = JugadorJuegoLogro.objects.all()
    serializer_class = JugadorJuegoLogroSerializer


class JugadorJuegoLogroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JugadorJuegoLogro.objects.all()
    serializer_class = JugadorJuegoLogroSerializer


class DiaList(generics.ListCreateAPIView):
    queryset = Dia.objects.all()
    serializer_class = DiaSerializer


class DiaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dia.objects.all()
    serializer_class = DiaSerializer


class JugadorJuegoList(generics.ListCreateAPIView):
    queryset = JugadorJuego.objects.all()
    serializer_class = JugadorJuegoSerializer


class JugadorJuegoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = JugadorJuego.objects.all()
    serializer_class = JugadorJuegoSerializer


#-------------------------------Clases----------------------------------------------------------------------------------


class SolicitudAmistadList(generics.ListCreateAPIView):
    queryset = SolicitudAmistad.objects.all()
    serializer_class = SolicitudAmistadSerializer


class SolicitudAmistadDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = SolicitudAmistad.objects.all()
    serializer_class = SolicitudAmistadSerializer


class MensajeList(generics.ListCreateAPIView):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer


class MensajeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mensaje.objects.all()
    serializer_class = MensajeSerializer


class JugadorList(generics.ListCreateAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer


class JugadorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Jugador.objects.all()
    serializer_class = JugadorSerializer


class MisionList(generics.ListCreateAPIView):
    queryset = Mision.objects.all()
    serializer_class = MisionSerializer


class MisionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Mision.objects.all()
    serializer_class = MisionSerializer


class RecompensaList(generics.ListCreateAPIView):
    queryset = Recompensa.objects.all()
    serializer_class = RecompensaSerializer


class RecompensaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recompensa.objects.all()
    serializer_class = RecompensaSerializer


class LogroList(generics.ListCreateAPIView):
    queryset = Logro.objects.all()
    serializer_class = LogroSerializer


class LogroDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Logro.objects.all()
    serializer_class = LogroSerializer


class JuegoList(generics.ListCreateAPIView):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer


class JuegoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Juego.objects.all()
    serializer_class = JuegoSerializer


class NotificacionList(generics.ListCreateAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer


class NotificacionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer


def info_lol(request, region, nombre):
    if request.method == 'GET':
        responseUsuario = requests.get("https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+nombre+"?api_key=RGAPI-1ea1f0b7-f93c-4f9b-bd8d-64d4c8f74799")
        if responseUsuario.status_code == 200:
            jsonUsuario = responseUsuario.json()
            responseMastery = requests.get("https://"+region+".api.riotgames.com/lol/champion-mastery/v4/scores/by-summoner/"+jsonUsuario['id']+"?api_key=RGAPI-1ea1f0b7-f93c-4f9b-bd8d-64d4c8f74799")
            if responseMastery.status_code == 200:
                nuevo = JuegoC(jsonUsuario['summonerLevel'], jsonUsuario['name'], region, responseMastery.json())

                serializer = JuegoSerializer(data=nuevo)
                if serializer.is_valid():
                    serializer.save()
                    return JsonResponse(nuevo, status=200, safe=False)
        else:
            return HttpResponse(status=404)