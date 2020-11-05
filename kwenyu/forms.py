from django import forms
from .models import Profile,Business
class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user','neighbourhood','status']

class NewBusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','neighbourhood']