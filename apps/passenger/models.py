from django.db import models
from apps.user.models import MyUser
from apps.uber.models import Location


class Passenger(models.Model):
     name = models.ForeignKey(MyUser,on_delete = models.CASCADE)
     image = models.ImageField(upload_to = 'ProfilePicture/')
     locations = models.ForeignKey(Location,on_delete = models.CASCADE)
     contact_info = models.CharField(max_length = 50)