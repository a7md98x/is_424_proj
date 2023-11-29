from curses.ascii import US
from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import *
from .forms import *
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth import authenticate, login as auth_login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from itertools import chain




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

def register1(request):
    if request.method == 'POST':  
            username = request.POST.get("username")
            password = request.POST.get("password")
            first_name = request.POST.get("first_name")
            last_name = request.POST.get("last_name")
            email = request.POST.get("email")

            print(f"Received username: {username}, password: {password} email: {email} fname:{first_name} lname :{last_name}")
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
            user.save()
            
            customer = customers.objects.create(
                first_name=first_name,
                last_name=last_name,
                email=email,
                user=user
            )
   

    return render(request, "app1/register.html")
            
            
            
            
            
            
def customer(request):
    customer_list = customers.objects.all()
    user_list = User.objects.all()
    customer_form = CustomerForm()
    return render(request,"app1/customer.html",{
        "customers_list": customer_list,"customer_form" :customer_form,'user_list':user_list
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
      

def book_details(request, book_id):
    book_obj = get_object_or_404(book, pk=book_id)

    return render(request, 'app1/book_details.html', {'book':book_obj})
      
          
            
# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
        
#         if form.is_valid():
#             form.save()
            
#             # Redirect to a success page or login page
#             return HttpResponseRedirect(reverse("app1:register"))
#     else:
#         form = UserCreationForm()

#     return render(request, "app1/register.html", {'form': form})



def details(request, username):
    user = get_object_or_404(User, username=username)
    customer = get_object_or_404(customers, user=user)
 
    customer_list = customers.objects.all()
    user_list = User.objects.all()

    available_books = book.objects.exclude(customers=customer)

    print(customer_list)
    print(user_list)
    if request.method == 'POST':
        book_id = request.POST.get('book')

        if book_id:
            
                book_to_add = book.objects.get(pk=book_id)
                customer.books.add(book_to_add)
                return redirect('app1:details', username=username)
           

    return render(request, 'app1/details.html', {'customer': customer, 'customer_list': customer_list, 'available_books': available_books,})






