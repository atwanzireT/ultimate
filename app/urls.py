from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('registration/', views.registration, name='registration'),	
    path('registerdashboard/', views.registerDashboard, name='registerdashboard'),
    path('register_district/', views.register_district, name='register_district'),
    path('register_village/', views.register_village, name='register_village'),
    path('register_country/', views.register_country, name='register_country'),
    path('register_plot/', views.register_plot, name='register_plot'),
    path('register_plot_owner/', views.register_plot_owner, name='register_plot_owner'),
    path('notification/', views.notification, name='notificaton'),
    path('appointment/', views.appointment, name='appointment'),
    path('update/', views.update, name='update'),
]