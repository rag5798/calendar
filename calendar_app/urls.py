from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.calendar_view, name='calendar'),
    path('add/', views.add_task_view, name='add_task'),
]