
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('create_locataire', views.create_locataire, name='create_locataire'),
    path('locataire/delete/<int:id>', views.delete, name="delete"),
    path('locataire/update/<int:id>', views.update, name="update"),

]
