from email.policy import default
from secrets import choice
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


GENDER_CHOICE = (
    ("", "Select Gender"),
    ("male", "male"),
    ("female", "female"),
)

class SignupForm(UserCreationForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length = 50)
    last_name = forms.CharField(max_length = 50)
    nationality = forms.CharField(max_length=50)
    phonenumber = forms.CharField(max_length=13, help_text="+256 #")
    gender = forms.ChoiceField(choices=GENDER_CHOICE)
    address = forms.CharField(max_length=50)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class EditUserForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    nationality = forms.CharField(max_length=50)
    phonenumber = forms.CharField(max_length=13, help_text="+256 #")
    gender = forms.ChoiceField(choices=GENDER_CHOICE)
    address = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'nationality', 'phonenumber', 'gender', 'address', 'is_active')
