from django.urls import path
from . import views

urlpatterns = [
  path('search/', views.search, name='search'),
  path('archive/', views.archive, name='archive'),
    path('', views.index, name='index'), 
]