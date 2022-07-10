from django.contrib import admin

from app.models import *

# Register your models here.
admin.site.register(Country)
admin.site.register(District)
admin.site.register(Village)
admin.site.register(Plot)
# admin.site.register(Plot_Owner)
admin.site.register(Registration)
admin.site.register(Notification)
admin.site.register(Appointment)
admin.site.register(Update)
# admin.site.register(Clerk)