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

Third_Party_Type = (
    ("", "Select Third Party Access"),
    ("client", "client"),
    ("clerk", "clerk"),
)

class EditUserForm(UserChangeForm):
    email = forms.EmailField()
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    nationality = forms.CharField(max_length=50)
    phonenumber = forms.CharField(max_length=13, help_text="+256 #")
    gender = forms.ChoiceField(choices=GENDER_CHOICE)
    address = forms.CharField(max_length=50)
    is_active = forms.BooleanField(default=False)
    Third_Party_Type = forms.ChoiceField(choice = Third_Party_Type)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email',
                  'nationality', 'phonenumber', 'gender', 'address', 'is_active')
