from django.db import models
import uuid
from users.models import User, Profile, Location
from .consts import MOBILE_BRANDS, CONDITION_OF_MOBILE, BOX, WARRANTY, CHARGER
from .utils import user_listing_path

class Listing(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    seller = models.ForeignKey(Profile, on_delete=models.CASCADE)
    brand = models.CharField(max_length=24, choices=MOBILE_BRANDS, default=None)
    price = models.IntegerField(default=0)
    model = models.CharField(max_length=64)
    color = models.CharField(max_length=24)
    warranty = models.CharField(max_length=24, choices=WARRANTY, default=None)
    box = models.CharField(max_length=24, choices=BOX, default=None)
    charger = models.CharField(max_length=24, choices=CHARGER, default=None)
    condition = models.CharField(max_length=24, choices=CONDITION_OF_MOBILE, default=None)
    location = models.OneToOneField(Location, on_delete=models.SET_NULL, null=True)
    image = models.ImageField(upload_to=user_listing_path)
    description = models.TextField(default="")
    
    def __str__(self):
        return f"{self.seller.user.username}\'s Listing - {self.model}"
    
class LikedListing(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    listing = models.ForeignKey(Listing, on_delete=models.CASCADE)
    like_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.listing.model} Listing liked by {self.profile.user.username}'