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
class Registration(models.Model):
    pass
