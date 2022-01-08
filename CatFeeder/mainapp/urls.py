from django.urls import path
from . import views

app_name = "mainapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('manual_time', views.manual_time, name='manual_time'),
    ]