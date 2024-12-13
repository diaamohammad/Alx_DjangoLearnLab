from rest_framework import routers
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView , AuthorView
from django.urls import path ,include

urlpatterns = [
    # مسارات للكتب
    path('books/', BookListCreateView.as_view(), name='book-list-create'),
    path('books/<int:pk>/', BookRetrieveUpdateDestroyView.as_view(), name='book-detail-update-destroy'),
    
    # مسارات للمؤلفين
    path('authors/', AuthorListCreateView.as_view(), name='author-list-create'),
    path('authors/<int:pk>/', AuthorRetrieveView.as_view(), name='author-detail'),
]
