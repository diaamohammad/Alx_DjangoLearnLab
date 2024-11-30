from django.contrib import admin

from .models import Book,Librarian,Library,Author

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Library)
admin.site.register(Librarian)


