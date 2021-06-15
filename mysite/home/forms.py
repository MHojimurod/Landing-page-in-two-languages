from django import forms
from .models import Subscribres



class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribres
        fields = ['email']
