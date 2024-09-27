from django import forms
from .models import Location
from localflavor.pk.forms import PKPostCodeField
from django.contrib.auth.models import User
from django import forms
# from users.widgets import CustomPictureImageFieldWidget
from .models import Location, Profile

class UserForm(forms.ModelForm):
    username = forms.CharField(disabled=True)
    first_name = forms.CharField(disabled=True)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')
    
class ProfileForm(forms.ModelForm):
    # photo = forms.ImageField(widget=CustomPictureImageFieldWidget)
    bio = forms.TextInput()

    class Meta:
        model = Profile
        fields = ('photo', 'bio', 'phone_number')

class LocationForm(forms.ModelForm):
    zip_code = PKPostCodeField(max_length=5, required=True)
    class Meta:
        model = Location
        fields = ['address_1', 'address_2', 'city', 'state', 'zip_code']
        
