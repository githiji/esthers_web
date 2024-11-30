from django import forms
from .models import Tweet

class TweetForm(forms.ModelForm):
    class meta:
        model = Tweet
        fields = ['tweet']
        widgets = {
            'tweet': forms.Textarea(attrs={'class': 'form-control'}),
        }