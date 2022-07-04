from http import client
from django.shortcuts import render
from .models import *
from datetime import datetime
from django.utils import timezone


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