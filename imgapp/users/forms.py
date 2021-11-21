from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email= forms.EmailField()
    DATE_INPUT_FORMATS = ['%d/%m/%Y']
    dob=forms.DateField(input_formats=DATE_INPUT_FORMATS)
    
    class Meta:
        model=User
        fields=['username','email','dob','password1','password2']