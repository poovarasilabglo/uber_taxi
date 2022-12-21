from django.contrib import admin
from apps.passenger.models import Passenger


class Passengeradmin(admin.ModelAdmin):
    list_display = ('id','name','image')
admin.site.register(Passenger,Passengeradmin)

