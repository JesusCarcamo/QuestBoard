from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),

    #-------------------------------clases------------------------------------------------------------------------------
    path('solicitud_amistad/', views.SolicitudAmistadList.as_view()),
    path('solicitud_amistad/<int:pk>', views.SolicitudAmistadDetail.as_view()),
    path('mensaje/', views.MensajeList.as_view()),
    path('mensaje/<int:pk>', views.MensajeDetail.as_view()),
    path('jugador/', views.JugadorList.as_view()),
    path('jugador/<int:pk>', views.JugadorDetail.as_view()),
    path('mision/', views.MisionList.as_view()),
    path('mision/<int:pk>', views.MisionDetail.as_view()),
    path('recompensa/', views.RecompensaList.as_view()),
    path('recompensa/<int:pk>', views.RecompensaDetail.as_view()),
    path('logro/', views.LogroList.as_view()),
    path('logro/<int:pk>', views.LogroDetail.as_view()),
    path('juego/', views.JuegoList.as_view()),
    path('juego/<int:pk>', views.JuegoDetail.as_view()),
    path('notificacion/', views.NotificacionList.as_view()),
    path('notificacion/<int:pk>', views.NotificacionDetail.as_view()),
    #--------------------------clases de asociacion---------------------------------------------------------------------
    path('mision_recompensa/', views.MisionRecompensaList.as_view()),
    path('mision_recompensa/<int:pk>', views.MisionRecompensaDetail.as_view()),
    path('jugador_recompensa/', views.JugadorRecompensaList.as_view()),
    path('jugador_recompensa/<int:pk>', views.JugadorRecompensaDetail.as_view()),
    path('jugador_juego_logro/', views.JugadorJuegoLogroList.as_view()),
    path('jugador_juego_logro/<int:pk>', views.JugadorJuegoLogroDetail.as_view()),
    path('dia/', views.DiaList.as_view()),
    path('dia/<int:pk>', views.DiaDetail.as_view()),
    path('jugador_juego/', views.JugadorJuegoList.as_view()),
    path('jugador_juego/<int:pk>', views.JugadorJuegoDetail.as_view()),
    path('league/<str:region>/<str:nombre>', views.info_lol)
]
