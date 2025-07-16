from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()
    phone=forms.CharField(max_length=255)
    address=forms.CharField(max_length=255)
    firstname=forms.CharField(max_length=20)
    lastname=forms.CharField(max_length=20)
    class Meta:
        model=User
        fields=['email','phone','address','firstname','lastname']
