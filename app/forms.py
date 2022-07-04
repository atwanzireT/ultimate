from django import forms
from .models import *

class Register_LandForm(forms.ModelForm):
    class Meta:
        model = Registration
        fields =('plot', 'owner', 'agreement_document')

# class Register_UserForm(forms.ModelForm):
#     class Meta:
#         model = Registration
#         fields =('plot', 'owner', 'agreement_document')