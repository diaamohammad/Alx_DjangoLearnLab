from django.db import models

class Author(models.model):
    name = models.CharField(max_length=10)
    def __str__(self):
        return self.name
class Book(models.model):
    title = models.CharField(max_length=10)
    publication_year = models.IntegerField()
    author =  models.ForeignKey(Author,on_delete=models.CASCADE)

    search_fields = ['title', 'author']
    ordering = ['title', 'publication_year']
    
    def __str__(self):
        return self.title