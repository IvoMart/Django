from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  #return HttpResponse("Hola Mundo!")
  return render(request, "hola/index.html")

def harry(request):
  return HttpResponse(
    '<h1>¡Hola Harry!<h1>'
    )

def hermione(request):
  return HttpResponse("<h1>¡Hola Hermione!</h1>")

#saludo a nombres ingresados en la direccion del Navegador
def saludar(request, nombre):
  '''return HttpResponse(f'Hola, {nombre.capitalize()}')'''
  return render(
    request,
    "hola/saludar.html",
    {"nombre": nombre.upper()}
  )