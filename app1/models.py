from django.db import models

# Create your models here.
class customers(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    username = models.CharField(max_length=30, unique = True)
   

    books = models.ManyToManyField("book", blank=True,related_name='customers')
    def __str__(self):
        return f"{self.first_name} {self.last_name} : { self.username}"


class book(models.Model):
    bname = models.CharField(max_length=64)
    def __str__(self):
        
        return f"{self.bname}"


