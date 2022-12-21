from django.contrib import admin
from apps.uber.models import Driver


class Driveradmin(admin.ModelAdmin):
    list_display = ('name','bio','image','contact_info')
admin.site.register(Driver,Driveradmin)


