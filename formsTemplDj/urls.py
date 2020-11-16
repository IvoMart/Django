from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="inicio" ),
    #Direccion para un Saludo Personalizado: Harry
    path("harry",views.harry, name="harry" ),
    #Direccion para un Saludo Personalizado: Hermione
    path("hermione",views.hermione, name="hermione" ),
    #Direccion para un Saludo Personalizado: Cualquier nombre ingresado en la direccion del Naveg.
    path("hola-<str:nombre>", views.saludar , name="saludar"),
]
