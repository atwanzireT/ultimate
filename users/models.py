from turtle import update
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from phone_field import PhoneField

# Create your models here.
class Profile(models.Model):
    GENDER_CHOICE = (
        ("", "Select Gender"),
        ("male", "male"),
        ("female", "female"),
    )

    USERTYPE_CHOICE = (
        ("", "Select Gender"),
        ("admin", "admin"),
        ("plot_owner", "plot_owner"),
        ("clerk", "clerk")
    )
    # add additional fields here'
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # username = models.CharField(max_length = 50, unique = True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', blank=True)
    email = models.EmailField(_("Email Address"), unique=True, blank=True)
    about = models.TextField(default="No About ...")
    address = models.CharField(blank=True, null=True, max_length=100)
    nationality = models.CharField(blank=True, null=True, max_length=100)
    phonenumber = PhoneField(blank=True, help_text='Contact phone number')
    gender = models.CharField(choices=GENDER_CHOICE, max_length=30, blank=True)
    user_type = models.CharField(choices=USERTYPE_CHOICE, max_length=30, blank=True)
    twitter = models.CharField(max_length=3000, null=True, blank=True)
    facebook = models.CharField(max_length=3000, null=True, blank=True)
    linkedin = models.CharField(max_length=3000, null=True, blank=True)
    instagram = models.CharField(max_length=3000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    def __str__(self) -> str:
        return self.user.username