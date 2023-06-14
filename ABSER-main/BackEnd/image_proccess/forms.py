from django import forms
from .models import image


class ImageForm(forms.ModelForm):
    """Form for the image model"""
    class Meta:
        model = image
        fields = ('image')