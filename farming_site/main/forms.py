from django import forms
from .models import Crop

class CropForm(forms.ModelForm):
    class Meta:
        model = Crop
        fields = ['name', 'quantity', 'price', 'image']
        labels = {
            'name': ' Name',
            'quantity': 'Quantity',
            'price': 'Price',
            'image': 'Image',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'}),
        }
    
