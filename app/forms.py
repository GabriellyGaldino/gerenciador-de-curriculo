from django.forms import ModelForm 
from django import forms 
from .models import User

class RegistrationForm(forms.ModelForm):
        
    class Meta:
        model = User
        fields = ('username', 'email')