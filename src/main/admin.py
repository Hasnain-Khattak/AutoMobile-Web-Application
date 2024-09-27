from django.contrib import admin
from .models import Listing, LikedListing

class ListingAdmin(admin.ModelAdmin):
    list_display = ('model', 'display_price', 'condition', 'description')  # Assuming these fields exist in your model
    readonly_fields = ('id', )

    def display_price(self, obj):
        return f"Rs {obj.price}"
    display_price.short_description = 'Price'
    

class LikedListingAdmin(admin.ModelAdmin):
    readonly_fields = ('id', )

admin.site.register(Listing, ListingAdmin)
admin.site.register(LikedListing, LikedListingAdmin)