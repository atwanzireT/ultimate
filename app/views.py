from http import client
from django.shortcuts import render
from .models import *
from datetime import datetime
from django.utils import timezone
from .forms import AppointmentForm, NotificationForm, Register_LandForm, Register_Plot_Owner, Register_Update, Register_country, Register_district, Register_village
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

def registerDashboard(request):
    return render(request, 'registerdashboard.html')

def register_country (request):
    form = Register_country(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()  #save data to table
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/')
    form = Register_country
    context={'form':form}
    return render(request, 'register_country.html', context)

def register_country (request):
    form = Register_country(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()  #save data to table
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/')
    form = Register_country
    context={'form':form}
    return render(request, 'register_country.html', context)

def register_district(request):
    form = Register_district(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()  #save data to table
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/')
    form = Register_district
    context={'form':form}
    return render(request, 'register_district.html', context)

def register_village(request):
    form = Register_village(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()  #save data to table
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/')
    form = Register_village
    context={'form':form}
    return render(request, 'register_village.html', context)

def register_plot(request):
    form = register_plot(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()  #save data to table
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/')
    form = register_plot
    context={'form':form}
    return render(request, 'register_plot.html', context)

def register_plot_owner(request):
    form = register_plot_owner(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()  #save data to table
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/')
    form = Register_Plot_Owner
    context={'form':form}
    return render(request, 'register_plot_owner.html', context)

def notification(request):
    form = NotificationForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()  #save data to table
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/')
    form = NotificationForm
    context={'form':form}
    return render(request, 'notification.html', context)

def appointment(request):
    form = AppointmentForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()  #save data to table
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/')
    form = AppointmentForm
    context={'form':form}
    return render(request, 'appointment.html', context)

def update(request):
    form = Register_Update(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()  #save data to table
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/')
    form = Register_district
    context={'form':form}
    return render(request, 'update.html', context)