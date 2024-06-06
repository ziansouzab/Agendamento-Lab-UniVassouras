from django.urls import include, path

from . import views


app_name = 'agenda'

urlpatterns = [
    path('', views.user_login, name='user_login'),
    path('agenda/', views.agenda_view, name='agenda_view')
]

