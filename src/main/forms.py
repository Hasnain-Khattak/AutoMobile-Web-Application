from django import forms
from .models import Listing
from .consts import MOBILE_BRANDS, CONDITION_OF_MOBILE, BOX, WARRANTY, CHARGER

class ListingForm(forms.ModelForm):
    image = forms.ImageField(required=True)
    price = forms.IntegerField(max_value=99999999, required=True)
    
    # Define the order of fields
    brand = forms.ChoiceField(choices=MOBILE_BRANDS)
    model = forms.CharField(max_length=64)
    color = forms.CharField(max_length=24)
    warranty = forms.ChoiceField(choices=WARRANTY)
    box = forms.ChoiceField(choices=BOX)
    charger = forms.ChoiceField(choices=CHARGER)
    condition = forms.ChoiceField(choices=CONDITION_OF_MOBILE)
    description = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = Listing
        fields = ['brand', 'model', 'color', 'warranty', 'box', 'charger', 'condition', 'price','image', 'description']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['price'].label = 'Price in PKR'