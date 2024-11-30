from django.db import models

# Create your models here.


class Author(models.Model):

    name = models.CharField(max_length=100,default='ahmed') 

class Book(models.Model):

    title = models.CharField(max_length=100,default='earth') 
    author = models.ForeignKey(Author,on_delete=models.CASCADE,null=True)

class Library(models.Model):

    name = models.CharField(max_length=100,default='readbook') 
    books = models.ManyToManyField(Book)

class Librarian(models.Model):
    name = models.CharField(max_length=100,default='ali') 
    library = models.OneToOneField(Library,on_delete=models.CASCADE,null=True)
