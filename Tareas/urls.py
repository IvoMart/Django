from django.urls import path
from Tareas import views

urlpatterns = [
    path("", views.home, name="home")
]
