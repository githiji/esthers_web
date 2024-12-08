from django import forms
from main.models import Tweet

class TweetForm(forms.ModelForm):
    class meta:
        model = Tweet
        fields = ['content']
        widgets = {
            'tweet': forms.Textarea(attrs={'class': 'form-control'}),
        }