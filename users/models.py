from django.db import models
from django.contrib.auth.models import AbstractUser, AbstractBaseUser, PermissionsMixin
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(AbstractUser):
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
    username = models.CharField(max_length = 50, unique = True)
    avatar = models.ImageField(upload_to='avatar/%Y/%m/%d', blank=True)
    email = models.EmailField(_("Email Address"), unique=True)
    bio = models.TextField(max_length=500)
    about = models.TextField(default="No About ...")
    gender = models.CharField(choices=GENDER_CHOICE)
    user_type = models.CharField(choices=USERTYPE_CHOICE)
    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    # USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS  = ['username']

    class Meta(AbstractUser.Meta):
       swappable = 'AUTH_USER_MODEL'

    def __str__(self) -> str:
        return self.username