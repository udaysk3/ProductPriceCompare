from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('searchByGTIN', views.searchByGTIN, name='searchByGTIN'),
]