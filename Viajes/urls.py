from django.urls import path
from Viajes import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    path("vuelos-lista", views.lista_vuelos, name="vueloLista"),
    path("vuelo-filtro-<int:vuelo_id>", views.filtra_vuelos, name="vueloFiltra"),
    path("aeropuertos-lista", views.lista_aerop, name="aeropsLista"),
]
