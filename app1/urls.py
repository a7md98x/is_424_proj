from django.urls import path
from django.views import View
from .  import views 

urlpatterns = [
    path("",views.index,name= 'index'),
    path('customer/<int:cid>', views.customer, name='customer'),
    path('books/', views.books, name='books'),
    path("login/",views.login, name="login")

]