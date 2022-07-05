from django.shortcuts import render
from django.contrib.auth import logout
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import *
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.views import generic
from django.urls import reverse_lazy
from django.http.response import HttpResponse, HttpResponseRedirect
from .forms import SignupForm

# Create your views here.
def login(request):
    return render(request, 'login.html', {})

def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')

def logout_page(request):
    return render(request, 'logout_user.html')

def Profile(request):
	return render(request, 'profile.html')
class UserRegistrationView(generic.CreateView):
	form_class = SignupForm
	template_name = 'registration/registration.html'
	success_url = reverse_lazy('success_main')

class UserEditView(generic.CreateView):
	form_class = UserChangeForm
	template_name = 'registration/edit_profile.html'
	success_url = reverse_lazy('success_main')

	def get_object(self):
		return self.request.user
