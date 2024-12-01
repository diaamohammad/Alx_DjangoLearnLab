from django.contrib.auth.decorators import permission_required,has_permission
from django.shortcuts import render, redirect
from .models import Book


# Create your views here.


["book_list", "raise_exception", "books"]
["from .forms import ExampleForm"]
@permission_required('app_name.can_edit', raise_exception=True)
def edit_view(request, pk):
    # View code here
    return render(request, 'edit_template.html')


def edit_view(request, pk):
    if not has_permission(request.user, 'app_name.can_edit'):
        return redirect('permission_denied')
    # View code here
    return render(request, 'edit_template.html')

def list_books(request):
    books = Book.objects.all() 
    context = {'book_list': books} 
    return render(request, 'relationship_app/list_books.html', context)