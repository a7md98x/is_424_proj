from dataclasses import fields
from turtle import mode
from django import forms
from .models import *

class LoginForm(forms.ModelForm):
    class Meta:
        model = customers
        fields = ['first_name','username']

class CustomerForm(forms.ModelForm):
    class Meta:
        model = customers
        fields = '__all__'
    

class BookForm(forms.ModelForm):
    class Meta:
        model = book
        fields = '__all__'
