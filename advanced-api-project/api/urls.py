from rest_framework import routers
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView , AuthorView
from django.urls import path ,include

router = routers.DefaultRouter()
router.register(r'books', ListView, basename='books')
router.register(r'books/(?P<pk>\d+)', DetailView, basename='books_detail')  # Use pk instead of id here
router.register(r'books/create', CreateView, basename='create')
router.register(r'books/update/(?P<pk>\d+)', UpdateView, basename='update')
router.register(r'books/delete/(?P<pk>\d+)', DeleteView, basename='delete')
router.register(r'authors', AuthorView, basename='authors')  # Changed 'users' to 'authors'

urlpatterns = [
    path('', include(router.urls))
]
