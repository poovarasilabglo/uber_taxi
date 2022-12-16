from django.contrib import admin
from apps.uber.models import Driver,Car,Location


class Driveradmin(admin.ModelAdmin):
    list_display = ('name','bio','image','vehicle','passenger_location','contact_info', 'status')
admin.site.register(Driver,Driveradmin)


class Caradmin(admin.ModelAdmin):
    list_display = ('car_brand','number_plate','seat_number')
admin.site.register(Car,Caradmin)


class Locationadmin(admin.ModelAdmin):
    list_display = ('id','pickup_location','dropoff_location')
admin.site.register(Location,Locationadmin)

