from dataclasses import fields
from turtle import mode
from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User as AuthUser


# class UserCreationForm(UserCreationForm):

#     password1 = forms.CharField(
#         label="Password",
#         strip=False,
#         widget=forms.PasswordInput,
#     )
#     password2 = forms.CharField(
#         label="Password confirmation",
#         widget=forms.PasswordInput,
#         strip=False,
#     )

#     class Meta:
#         model = customers
#         fields =  '__all__'


class CustomerForm(forms.ModelForm):
    class Meta:
        model = customers
        fields =['first_name', 'last_name', 'email']
    

class BookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = '__all__'

