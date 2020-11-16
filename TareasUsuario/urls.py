from django.urls import path
from . import views

urlpatterns = [
    path("", views.home , name="hometarea"),
    path("agregar", views.masTareas , name="agregar"),
]
