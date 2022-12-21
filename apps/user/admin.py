from django.contrib import admin
from apps.user.models import MyUser


class MyUseradmin(admin.ModelAdmin):
    list_display = ('id','username','is_uber','is_driver','is_passenger')
admin.site.register(MyUser,MyUseradmin)


