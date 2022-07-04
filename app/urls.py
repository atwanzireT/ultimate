from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('registration/', views.registration, name='registration'),	
    path('registerdashboard/', views.registerDashboard, name='registerdashboard'),	
]