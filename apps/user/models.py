from django.db import models
from django.contrib.auth.models import AbstractUser


class MyUser(AbstractUser):
     is_uber = models.BooleanField(default=False)
     is_passenger = models.BooleanField(default=False)
     
