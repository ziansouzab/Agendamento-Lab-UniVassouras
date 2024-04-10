from django.urls import include, path

from .views import *


app_name= 'agenda'

urlpatterns = [
    path('', home, name="home"),
]

