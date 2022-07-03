from distutils.command.upload import upload
from email.mime import image
from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Location models
class Country(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.name

class District(models.Model):
    name = models.CharField(max_length=50)
    countryid = models.ForeignKey(Country, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
class Village(models.Model):
    name = models.CharField(max_length=50)
    districtid = models.ForeignKey(District, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

# plots
class Plot(models.Model):
    plot_number = models.CharField(max_length=50)
    size = models.CharField(help_text="width X height", max_length=50)
    location = models.ForeignKey(Village, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.plot_number

# registration
class Plot_Owner(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user

class Registration(models.Model):
    plot = models.ForeignKey(Plot, on_delete=models.CASCADE)
    secret_code = models.UUIDField(unique=True)
    owner = models.ForeignKey(Plot_Owner, on_delete=models.CASCADE)
    registedBy = models.ForeignKey(User, on_delete=models.CASCADE)
    agreement_document = models.FileField(help_text="Agreement to the plot of Land Scanned")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.plot
     
class Feedback(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    body = models.TextField()
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Appointments(models.Model):
    title = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    detail = models.TextField()
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title

class Updates(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = "updates")
    detail = models.TextField()
    createdBy = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title