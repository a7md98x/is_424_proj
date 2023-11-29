from django.urls import path
from django.views import View
from .  import views 
app_name = "app1"
urlpatterns = [
    path("",views.index,name= 'index'),
    path('customer/<int:cid>', views.customer, name='customer'),
    path('books/', views.books, name='books'),
    path("login/",views.login, name="login"),
    path("register/",views.register, name="register"),
    path("addBook/",views.add_books, name="add_book"),
    path("customers/<int:customer_id>/", views.details, name="details"),
    path('add_customer/', views.add_customer, name='add_customer'), 
    path('logout/', views.logout_view, name='logout'),




]