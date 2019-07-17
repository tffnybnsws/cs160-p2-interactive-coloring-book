from django.urls import path
from . import views

urlpatterns = [
  path('search/', views.search, name='search'),
  path('archive/', views.archive, name='archive'),
  path('aphextwin/', views.aphextwin, name='aphextwin'),
  path('ddealer', views.ddealer, name='ddealer'),
  path('', views.index, name='index'), 
]