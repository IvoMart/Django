from django.shortcuts import render
from django.http import HttpResponse

# Tareas Variables - Listado
Tareas = ["Salir a caminar", "Comprar Pan", "Practicar música"]
# Create your views here.
def home(request):
  return render(
    request,
    "inicio.html",
    {
      "tareas": Tareas
    }
  )