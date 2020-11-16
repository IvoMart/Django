from django.shortcuts import render
from django import forms
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.urls import reverse

#Listado Predefinido Tareas
#Tareas = ["Tarea1","Tarea2","Tarea3","Tarea4"]

# Create your views here.
def home( request ):
  #Para trabajar con las sessiones iniciadas, el listado es individual
  if "Tareas" not in request.session:
    request.session["Tareas"] = []
  
  return render(
    request,
    "index.html",
    {
      #"tarea":Tareas
      "tarea":request.session["Tareas"]
    }
  )

# Agrega tareas a la Lista
def masTareas(request):
  if request.method == "POST":
    form = NuevaTarea(request.POST)
    if form.is_valid():
      tarea = form.cleaned_data["tarea"]
      #Tareas.append(tarea)
      request.session["Tareas"] += [tarea]
      return HttpResponseRedirect(reverse("hometarea"))
    else:
      return render(
        request,
        "tareas/agregar.html",
        {
          "formulario":NuevaTarea()
        }
        )
    
  
  return render(
    request,
    "tareas/agregar.html",
    {
      "formulario":NuevaTarea()
    }
  )
  
class NuevaTarea(forms.Form):
  tarea = forms.CharField(label="Agregar Nueva Tarea")