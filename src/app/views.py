from django.shortcuts import render
from django.conf import settings
from .serializers import JugadorSerializer, MisionSerializer
from rest_framework.parsers import JSONParser
from .models import Jugador, Mision, Juego, Dia
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
# Create your views here.
def inicio(request):
    return render(request, "base.html")


@csrf_exempt
def jugadores_list(request):
    # Metodo que responde y envia peticiones en forma de lista de Jsons correspondientes con el modelo del producto
    if request.method == 'GET':
        # En caso de recibir una peticion de tipo GET
        # Solicita todos los productos a la base de datos
        jugadores = Jugador.objects.all()
        # Convierte el listado de modelos de productos a un listado de productos JSON
        serializer = JugadorSerializer(jugadores, many=True)
        # Retorna el listado de productos JSON en forma de respuesta HTTP
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # En caso de recibir una peticion POST
        # Convierte el JSon en un objeto de Python
        data = JSONParser().parse(request)
        # Convierte el objeto en un modelo de Producto
        serializer = JugadorSerializer(data=data)
        # Comprueba la validez del modelo
        if serializer.is_valid():
            # Guarda el objeto en la base de datos
            serializer.save()
            # Retorna el nuevo Objeto almacendao en la base de datos
            return JsonResponse(serializer.data, status=201)
        # Retorna una respuest de fallo
        return JsonResponse(serializer.errors, status=404)

@csrf_exempt
def misiones_list(request):
    # Metodo que responde y envia peticiones en forma de lista de Jsons correspondientes con el modelo del producto
    if request.method == 'GET':
        # En caso de recibir una peticion de tipo GET
        # Solicita todos los productos a la base de datos
        misiones = Jugador.objects.all()
        # Convierte el listado de modelos de productos a un listado de productos JSON
        serializer = MisionSerializer(misiones, many=True)
        # Retorna el listado de productos JSON en forma de respuesta HTTP
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # En caso de recibir una peticion POST
        # Convierte el JSon en un objeto de Python
        data = JSONParser().parse(request)
        # Convierte el objeto en un modelo de Producto
        serializer = MisionSerializer(data=data)
        # Comprueba la validez del modelo
        if serializer.is_valid():
            # Guarda el objeto en la base de datos
            serializer.save()
            # Retorna el nuevo Objeto almacendao en la base de datos
            return JsonResponse(serializer.data, status=201)
        # Retorna una respuest de fallo
        return JsonResponse(serializer.errors, status=404)

csrf_exempt    
def juego_list(request):
    # Metodo que responde y envia peticiones en forma de lista de Jsons correspondientes con el modelo del producto
    if request.method == 'GET':
        # En caso de recibir una peticion de tipo GET
        # Solicita todos los productos a la base de datos
        juegos = Juego.objects.all()
        # Convierte el listado de modelos de productos a un listado de productos JSON
        serializer = JuegoSerializer(productos, many=True)
        # Retorna el listado de productos JSON en forma de respuesta HTTP
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # En caso de recibir una peticion POST
        # Convierte el JSon en un objeto de Python
        data = JSONParser().parse(request)
        # Convierte el objeto en un modelo de Producto
        serializer = JuegoSerializer(data=data)
        # Comprueba la validez del modelo
        if serializer.is_valid():
            # Guarda el objeto en la base de datos
            serializer.save()
            # Retorna el nuevo Objeto almacendao en la base de datos
            return JsonResponse(serializer.data, status=201)
        # Retorna una respuest de fallo
        return JsonResponse(serializer.errors, status=404)

@csrf_exempt
def dias_list(request):
    # Metodo que responde y envia peticiones en forma de lista de Jsons correspondientes con el modelo del producto
    if request.method == 'GET':
        # En caso de recibir una peticion de tipo GET
        # Solicita todos los productos a la base de datos
        dias = Dia.objects.all()
        # Convierte el listado de modelos de productos a un listado de productos JSON
        serializer = DiaSerializer(productos, many=True)
        # Retorna el listado de productos JSON en forma de respuesta HTTP
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # En caso de recibir una peticion POST
        # Convierte el JSon en un objeto de Python
        data = JSONParser().parse(request)
        # Convierte el objeto en un modelo de Producto
        serializer = DiaSerializer(data=data)
        # Comprueba la validez del modelo
        if serializer.is_valid():
            # Guarda el objeto en la base de datos
            serializer.save()
            # Retorna el nuevo Objeto almacendao en la base de datos
            return JsonResponse(serializer.data, status=201)
        # Retorna una respuest de fallo
        return JsonResponse(serializer.errors, status=404)





































