from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('jugadores', views.jugadores_list),
    path('misiones', views.misiones_list),
]
