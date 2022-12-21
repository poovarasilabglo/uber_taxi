from django.db import models
from apps.user.models import MyUser


REQUESTED = 1
STARTED = 2
IN_PROGRESS = 3
COMPLETED = 4
TRIP_STATUS_CHOICES  = (
    (REQUESTED, 'Requested'),
    (STARTED, 'Started'),
    (IN_PROGRESS, 'In_Progress'),
    (COMPLETED, 'Completed'),
)


class TimeStampedModel(models.Model):
     created_on = models.DateTimeField(auto_now_add=True)
     updated_on = models.DateTimeField(auto_now=True)
     class Meta:
         abstract = True


class Driver(TimeStampedModel):
    name = models.OneToOneField(MyUser,on_delete = models.CASCADE)
    bio = models.FileField()
    image = models.ImageField(upload_to = 'profilepicture/')
    car_brand = models.CharField(max_length = 50)
    number_plate = models.CharField(max_length = 20)
    seat_number = models.CharField(max_length = 20)
    contact_info =models.CharField(max_length = 50)
    
    
    def __str__(self):
        return '{}'.format(self.car_brand)




