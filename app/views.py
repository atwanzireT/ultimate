from http import client
from django.conf import settings
from django.shortcuts import render
from matplotlib.style import context
from .models import *
from datetime import datetime
from django.utils import timezone
from .forms import *
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import permission_required
from django.core.mail import send_mail


# Create your views here.
@login_required(login_url='/profile/login/')
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

@login_required(login_url='/profile/login/')
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

@login_required(login_url='/profile/login/')
def registerDashboard(request):
    return render(request, 'registerdashboard.html')

@login_required(login_url='/profile/login/')
def register_success(request):
    return render(request, 'registerdashboard_success.html')

@login_required(login_url='/profile/login/')
def register_country (request):
    form = Register_countryForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()  #save data to table
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/success/')
    form = Register_countryForm
    context={'form':form}
    return render(request, 'register_country.html', context)

# def register_country (request):
#     form = Register_country(request.POST or None, request.FILES or None)
#     if request.method =='POST':
#         if form.is_valid():
#             form.save()  #save data to table
#             messages.success(request,"Registration Successful")
#             return HttpResponseRedirect('/')
#     form = Register_country
#     context={'form':form}
#     return render(request, 'register_country.html', context)

@login_required(login_url='/profile/login/')
def register_district(request):
    form = Register_districtForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()  #save data to table
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/success/')
    form = Register_districtForm
    context={'form':form}
    return render(request, 'register_district.html', context)

@login_required(login_url='/profile/login/')
def register_village(request):
    form = Register_villageForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()  #save data to table
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/success/')
    form = Register_villageForm
    context={'form':form}
    return render(request, 'register_village.html', context)

@login_required(login_url='/profile/login/')
def register_plot(request):
    form = Register_PlotForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()  #save data to table
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/success/')
    form = Register_PlotForm
    context={'form':form}
    return render(request, 'register_plot.html', context)

@login_required(login_url='/profile/login/')
def register_plot_owner(request):
    form =  Register_Plot_OwnerForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()  #save data to table
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/success/')
    form = Register_Plot_OwnerForm
    context={'form':form}
    return render(request, 'register_plot_owner.html', context)

@permission_required('auth.view_user')
def register_Clerk(request):
    form =  Register_ClerkForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            form.save()  #save data to table
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/success/')
    form = Register_ClerkForm
    context={'form':form}
    return render(request, 'register_clerk.html', context)

@login_required(login_url='/profile/login/')
def notification(request):
    form = NotificationForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            user = request.user
            obj = form.save(commit=False)
            obj.createdBy = request.user
            obj.save()  #save data to table
            form = NotificationForm
            try:
                subject = "Ultimate Notification"
                message = f"{user.username}, Thank you for contacting us. \n We will get to you shortly."
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email, ]
                send_mail(
                    subject, 
                    message, 
                    email_from, 
                    recipient_list,
                    fail_silently=False,
                )
            except:
                pass
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/success_main/')
    form = NotificationForm
    context={'form':form}
    return render(request, 'notify.html', context)


@login_required(login_url='/profile/login/')
def appointment(request):
    form = AppointmentForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.createdBy = request.user
            obj.save()  #save data to table
            form = AppointmentForm
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/success_main/')
    form = AppointmentForm
    context={'form':form}
    return render(request, 'create_appointment.html', context)

@login_required(login_url='/profile/login/')
def create_update(request):
    form = Create_UpdateForm(request.POST or None, request.FILES or None)
    if request.method =='POST':
        if form.is_valid():
            obj = form.save(commit=False)
            obj.createdBy = request.user
            obj.save()  #save data to table
            form = Create_UpdateForm
            messages.success(request,"Registration Successful")
            return HttpResponseRedirect('/success_main/')
    form = Create_UpdateForm
    context={'form':form}
    return render(request, 'create_update.html', context)

@login_required(login_url='/profile/login/')
def success_main(request):
    return render(request, 'success_main.html')

@login_required(login_url='/profile/login/')
def appointmentList(request):
    appointment = Appointment.objects.all()
    context = {
        "appointment":appointment,
    }
    return render(request, 'appointments.html', context)