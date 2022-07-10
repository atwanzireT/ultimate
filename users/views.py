import re
from django.shortcuts import render
from django.contrib.auth import logout
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views import generic
from django.urls import reverse_lazy
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import *
from app.models import * 

# Create your views here.
def login(request):
    return render(request, 'login.html', {})

def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')

def logout_page(request):
    return render(request, 'logout_user.html')

def Profile(request):
	user = request.user
	registration = Registration.objects.filter(owner_id__user_id = user.id)
	context = {
		"registration":registration,
	}
	return render(request, 'profile.html', context)
class UserRegistrationView(generic.CreateView):
	form_class = SignupForm
	template_name = 'registration/registration.html'
	success_url = reverse_lazy('success_main')

class UserEditView(generic.UpdateView):
	form_class = EditUserForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('success_main')

	def get_object(self):
		return self.request.user
		
class ProfileUpdate(generic.UpdateView):
	form_class = ProfileForm
	template_name = "registration/profile_update.html"
	success_url = reverse_lazy('success_main')

	def get_object(self):
		return self.request.user
		