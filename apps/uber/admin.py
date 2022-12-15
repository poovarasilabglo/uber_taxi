from django.contrib import admin
from apps.uber.models import Driver
from apps.user.models import MyUser


class Driveradmin(admin.ModelAdmin):
    list_display = ('bio','image','vehicle','passenger_location','contact_info','status')
admin.site.register(Driver,Driveradmin)


