from dataclasses import fields
from django import forms
from .models import *


class Register_LandForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields = ('plot', 'owner', 'agreement_document')

# class Register_UserForm(forms.ModelForm):
#     class Meta:
#         model = Registration
#         fields =('plot', 'owner', 'agreement_document')


class Register_countryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ('name',)


class Register_districtForm(forms.ModelForm):
    class Meta:
        model = District
        fields = ('name', 'countryid')


class Register_villageForm(forms.ModelForm):
    class Meta:
        model = Village
        fields = ('name', 'districtid')


class Register_PlotForm(forms.ModelForm):
    class Meta:
        model = Plot
        fields = ('plot_number', 'size', 'location')


class Register_ClerkForm(forms.ModelForm):
    class Meta:
        model = Clerk
        fields = ('user', 'bio', 'avatar')

class Register_Plot_OwnerForm(forms.ModelForm):
    class Meta:
        model = Plot_Owner
        fields = ('user', 'bio', 'avatar')


class NotificationForm(forms.ModelForm):
    class Meta:
        model = Notification
        fields = ('title', 'subject', 'body')


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ('title', 'subject', 'detail', 'book_day')


class Create_UpdateForm(forms.ModelForm):
    class Meta:
        model = Update
        fields = ('title', 'image', 'detail')
