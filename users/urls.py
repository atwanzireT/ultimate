from django.urls import path
from . import views
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout', views.logout_func, name='logout'),
    path('logoutpage', views.logout_page, name='logoutpage'),
    path('register', UserRegistrationView.as_view(), name = "register"),
    path('profile', views.Profile, name='profile'),
    path('<int:pk>/edit_profile', UserEditView.as_view(), name = "edit_profile"),
    path('password/', auth_views.PasswordChangeView.as_view(template_name = "edit_password.html")),
    path('<int:pk>/profile_update', ProfileUpdate.as_view(), name="profile_update"),
]