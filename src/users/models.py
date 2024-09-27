from django.db import models
from django.contrib.auth.models import User
from localflavor.pk.models import PKPostCodeField, PKStateField
from .utils import user_directory_path

class Location(models.Model):
    address_1 = models.CharField(max_length=100)
    address_2 = models.CharField(max_length=100, blank=True)
    city = models.CharField(max_length=64)
    state = PKStateField(default="PK-KP")
    zip_code = PKPostCodeField(blank=True)
    
    def __str__(self):
        return f"Location {self.id}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=user_directory_path, null=True)
    bio = models.CharField(max_length=200, blank=True)
    phone_number = models.CharField(max_length=11, blank=True)
    location = models.OneToOneField(Location, on_delete=models.CASCADE, null=True)
    
    def __str__(self):
        return f"{self.user.username}'s Profile"