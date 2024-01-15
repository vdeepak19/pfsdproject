from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Register)
admin.site.register(RentCar)
# admin.site.register(CustomUser)

#
# from django.contrib import admin
# from django.contrib.admin.models import LogEntry
#
# admin.site.unregister(LogEntry)
