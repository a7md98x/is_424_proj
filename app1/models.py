from django.db import models
from django.contrib.auth.models import User 
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator




# Create your models here.
class customers(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    email = models.CharField(max_length=64)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    books = models.ManyToManyField("book", blank=True,related_name='customers')
    def __str__(self):
        return f"{self.first_name} {self.last_name} : "


class book(models.Model):
    bname = models.CharField(max_length=64)
    author = models.CharField(max_length=100)
    pages = models.CharField(max_length=64)
    language = models.CharField(max_length=64)
    average_rating = models.FloatField(default=0.0, validators=[MaxValueValidator(10)])
    price = models.DecimalField(max_digits=10, decimal_places=2)
    edition = models.PositiveIntegerField()
    genre = models.CharField(max_length=64)
    ISBN = models.CharField(max_length=13, unique=True)






    def __str__(self):
        
        return f"{self.bname}"

