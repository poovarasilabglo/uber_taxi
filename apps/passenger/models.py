from django.db import models
from apps.user.models import MyUser
from apps.uber.models import Driver


REQUESTED = 1
STARTED = 2
IN_PROGRESS = 3
COMPLETED = 4
ACCEPTED = 5
CANCEL = 6
TRIP_STATUS_CHOICES  = (
    (REQUESTED, 'Requested'),
    (STARTED, 'Started'),
    (IN_PROGRESS, 'In_Progress'),
    (COMPLETED, 'Completed'),
    (ACCEPTED, 'Accepted'),
    (CANCEL, 'cancel')
)


class Passenger(models.Model):
    name = models.ForeignKey(MyUser, on_delete = models.CASCADE)
    driver = models.ForeignKey(Driver,on_delete = models.CASCADE)
    image = models.ImageField(upload_to = 'ProfilePicture/')
    pickup_location = models.CharField(max_length = 100)
    dropoff_location = models.CharField(max_length = 100)
    passenger_contact = models.CharField(max_length = 50)
    is_accepted = models.IntegerField(choices = TRIP_STATUS_CHOICES, default=1)
  
     
    def __str__(self):
       return '{}'.format(self.name)
    

    
    
   