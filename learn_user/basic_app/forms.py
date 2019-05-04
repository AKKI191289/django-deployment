from django import forms
from django.contrib.auth.models import User
from .models import UserNameInfo

class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','email','password')

class UserNameInfoForm(forms.ModelForm):
    class Meta():
        model=UserNameInfo
        fields=('portfolio_site','portfolio_image')
