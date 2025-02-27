from django import forms
from .models import Crop

class CropForm(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.IntegerField()
    quantity = forms.IntegerField()
    image = forms.ImageField()
    second_image = forms.ImageField(required=False)


