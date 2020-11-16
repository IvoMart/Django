from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def nwyear(request):
  fecha_actual = datetime.datetime.now();
  return render(
    request,
    "newYear/index.html",
    {"nuevoanio": fecha_actual.month == 1 and fecha_actual.day == 1
    })
  