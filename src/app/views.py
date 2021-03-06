from django.http import JsonResponse
from django.shortcuts import render, redirect

from rest_framework import generics
from .models import *
from .serializers import *

# Create your views here.
def inicio(request):
    return render(request, "base.html")

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

