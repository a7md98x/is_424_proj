from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.urls import reverse

# Create your views here.
def index (request):
    customer_form = CustomerForm()
    customer_list = customers.objects.all()
    return render(request,"app1/index.html",{
        "customers_list": customer_list,"customer_form" :customer_form
    })

def login(request):
    login_form = LoginForm()
    return render(request,"app1/login.html",{
        "login_form":login_form
    })
    
def customer(request, cid):
    customer_list = customers.objects.all()
    customer_form = CustomerForm()
    return render(request,"app1/customer.html",{
        "customers_list": customer_list,"customer_form" :customer_form
    })

def books(request):
    book_list = book.objects.all()
    book_form = BookForm()
    return render(request,"app1/book.html",{
        "book_list": book_list,"book_form" :book_form
    })