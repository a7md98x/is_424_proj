from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required



# Create your views here.
def index (request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))
    customer_form = CustomerForm()

    customer_list = customers.objects.all()
    return render(request,"app1/index.html",{
        "customers_list": customer_list,"customer_form" :customer_form
    })

def login(request):
    if request.method == 'POST':  
            username = request.POST.get("username")
            password = request.POST.get("password")

            print(f"Received username: {username}, password: {password}")

            user = authenticate(request, username=username, password=password)

            if user:
                print("fffff")
                auth_login(request, user)
                return HttpResponseRedirect(reverse("app1:books"))
            else:
                return render(request, "app1/login.html",
                              {"message":"invalid"})
            

    return render(request, "app1/login.html")
    
def customer(request, cid):
    customer_list = customers.objects.all()
    customer_form = CustomerForm()
    return render(request,"app1/customer.html",{
        "customers_list": customer_list,"customer_form" :customer_form
    })


@login_required 
def add_customer(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        if customer_form.is_valid():
            customer = customer_form.save(commit=False)
            customer.user = request.user  # Assign the logged-in user to the customer
            customer.save()
            
            return HttpResponseRedirect(reverse("app1:books"))
        
    else:
            customer_form = CustomerForm()
            
    return render(request, 'app1/add_customer.html', {'customer_form': customer_form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("app1:login"))



def books(request):
    book_list = book.objects.all()
    customer_list = customers.objects.all()

    book_form = BookForm()
    return render(request,"app1/book.html",{
        "book_list": book_list,"book_form" :book_form, "customers_list" : customer_list
    })


def add_books(request):
    if request.method == 'POST':
        book_form = BookForm(request.POST)
        if book_form.is_valid():
            book_form.save()
            book_form = BookForm() # reset form  after submiting
    else:
        book_form =  BookForm() 
    book_list = book.objects.all()
    return render(request, 'app1/add_book.html', {'book_list': book_list, 'book_form': book_form})
      
          
          
            
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            
            # Redirect to a success page or login page
            return HttpResponseRedirect(reverse("app1:register"))
    else:
        form = UserCreationForm()

    return render(request, "app1/register.html", {'form': form})



   
def details(request, customer_id):
    customer = get_object_or_404(customers, pk=customer_id)
    customer_list = customers.objects.all()

    available_books= book.objects.exclude(customers__in=[customer])

    if request.method == 'POST':
        book_id = request.POST['book']
        book_to_add = book.objects.get(pk=book_id)
        customer.books.add(book_to_add)
        return redirect('app1:details', customer_id=customer_id)

    return render(request, 'app1/details.html', {'customer': customer, 'customer_list': customer_list, 'available_books': available_books})






