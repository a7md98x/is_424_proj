from django.urls import path
from . import views

app_name = "app1"

urlpatterns = [
    path("", views.index, name='index'),
    path('customer/', views.customer, name='customer'),
    path('books/', views.books, name='books'),
    path("login/", views.login, name="login"),
    path("register/", views.register1, name="register"),
    path("addBook/", views.add_books, name="add_book"),
    path("customers/<str:username>/", views.details, name="details"),
    path('add_customer/', views.add_customer, name='add_customer'),
    path('logout/', views.logout_view, name='logout'),
    path('book_details/<int:book_id>/', views.book_details, name='book_details'),
]
