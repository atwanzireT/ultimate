from django.shortcuts import render
from django.contrib.auth import logout
from django.http.response import HttpResponse, HttpResponseRedirect

# Create your views here.
def login(request):
    return render(request, 'login.html', {})

def logout_func(request):
    logout(request)
    return HttpResponseRedirect('/')