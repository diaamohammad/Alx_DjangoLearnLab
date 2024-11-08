from django.contrib import admin
from . import Book
# Register your models here.
admin.site.register(Book)
class AuthorAdmin(admin.ModelAdmin):
    pass
class Book(admin.ModelAdmin):
    list_filter = ["author", "publication_year"]
    search_fields = ["title"]