from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home),
    path('searchByGTIN', views.searchByGTIN, name='searchByGTIN'),
    path('searchByKeyword',views.searchByKeyword,name="searchByKeyword"),
    path('sortByPrice',views.sortByPrice,name="sortByPrice"),
    path('filterByBudget',views.filterByBudget,name='filterByBudget')
]