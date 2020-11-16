from django.shortcuts import render
from Viajes.models import Vuelo, Aeropuerto

# Create your views here.
def inicio( request ):
  return render(
    request,
    "inicio.html"
  )

def lista_vuelos(request):
  return render(
    request,
    "vuelos/vuelos.html",
    {
      "viajes": Vuelo.objects.all()
    }
  )
  
def lista_aerop(request):
  return render(
    request,
    "vuelos/aeropuestos.html",
    {
      "aerops": Aeropuerto.objects.all()
    }
  )
  
def filtra_vuelos( request, vuelo_id ):
  return render(
    request,
    'vuelos/vuelo-filtro.html',
    {
      "vuelo": Vuelo.objects.get(id=vuelo_id)
    }
  )