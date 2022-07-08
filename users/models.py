from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.
class UserProfile(models.Model):
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
    user = models.OneToOneField(User, on_delete=models.DO_NOTHING)
    # username = models.CharField(max_length = 50, unique = True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', blank=True)
    email = models.EmailField(_("Email Address"), unique=True, blank=True)
    about = models.TextField(default="No About ...")
    gender = models.CharField(choices=GENDER_CHOICE, max_length=30)
    user_type = models.CharField(choices=USERTYPE_CHOICE, max_length=30)
    twitter = models.CharField(max_length=3000, null=True, blank=True)
    facebook = models.CharField(max_length=3000, null=True, blank=True)
    website = models.CharField(max_length=3000, null=True, blank=True)


    def __str__(self) -> str:
        return self.username