from django import forms
from .models import Flashes, Profile 


class ProfileForm(forms.ModelForm):
    class Meta:
        model= Profile
        exclude = ['user']