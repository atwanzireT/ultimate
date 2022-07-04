from http import client
from django.shortcuts import render
from .models import *
from datetime import datetime
from django.utils import timezone
from .forms import Register_LandForm
from django.contrib import messages
from django.http import HttpResponseRedirect


# Create your views here.
def index(request):
    # feedbacks = Notification.objects.filter(created = timezone.now).count()
    # appointments = Appointment.objects.filter(book_day = timezone.now).count()
    # clients = Plot_Owner.objects.filter(ThirdPartyType = "client", created = timezone.now).count()
    appointment_summary = Appointment.objects.all()[:10]
    updates = Update.objects.all()[:10]

    feedbacks_report = Notification.objects.all().count()
    appointments_report = Appointment.objects.all().count()
    clients_report = Plot_Owner.objects.all().count()
    dic = {
        # "feedbacks":feedbacks,
        # "appointments":appointments,
        # "clients":clients,
        'appointment_summary':appointment_summary,
        "updates":updates,
        "feedbacks_report":feedbacks_report,
        "appointments_report":appointments_report,
        "clients_report":clients_report,
    }
    return render(request, 'index.html', dic)

def registration (request):
    form = Register_LandForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.registedBy = request.user
            obj.save()  #save data to table
            form = Register_LandForm
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/')
    form = Register_LandForm
    context={'form':form}
    return render(request, 'registration.html', context)

def registerCard(request):
    return render(request, 'registercard.html')