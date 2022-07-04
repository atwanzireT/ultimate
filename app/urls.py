from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('registration/', views.registration, name='registration'),	
    path('registercards/', views.registerCard, name='registerCard'),	
]