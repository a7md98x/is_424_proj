from dataclasses import fields
from turtle import mode
from django import forms
from .models import *
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.models import User as AuthUser

class CustomerForm(forms.ModelForm):
    class Meta:
        model = customers
        fields =['first_name', 'last_name', 'email']
    

class BookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = '__all__'

class BookUpdateForm(forms.ModelForm):
    class Meta:
        model = book
        fields = '__all__'
