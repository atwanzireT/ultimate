from distutils.command.upload import upload
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
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class EditUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
