from django.urls import path
from newYear import views

urlpatterns = [
    path("new-year", views.nwyear, name="home"),
]
