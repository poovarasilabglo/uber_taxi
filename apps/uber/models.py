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


class Car(models.Model):
    car_brand = models.CharField(max_length = 50)
    number_plate = models.CharField(max_length = 20)
    seat_number = models.CharField(max_length = 20)
    
    def __str__(self):
        return self.car_brand


class Driver(TimeStampedModel):
    name = models.OneToOneField(MyUser,on_delete = models.CASCADE)
    bio = models.CharField(max_length = 100)
    image = models.ImageField(upload_to = 'profilepicture/')
    vehicle = models.ForeignKey(Car, on_delete = models.CASCADE)
    passenger_location = models.ForeignKey('Location', on_delete = models.CASCADE)
    contact_info =models.CharField(max_length = 50)
    status = models.IntegerField(choices = TRIP_STATUS_CHOICES,default = 1)
    
    def __str__(self):
         return '{} {} {}'.format(self.name,self.vehicle,self.passenger_location)


class Location(models.Model):
    pickup_location = models.CharField(max_length = 100)
    dropoff_location = models.CharField(max_length = 100)

    def __str__(self):
        return self.pickup_location



