from rest_framework import routers
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView , AuthorView
from django.urls import path ,include

urlpatterns =[
    path('books/',ListView.as_view(), name='book-list'), 
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),  # لعرض كتاب واحد
    path('books/create/', CreateView.as_view(), name='book-create'),  # لإنشاء كتاب جديد
    path('books/<int:pk>/update/', UpdateView.as_view(), name='book-update'),  # لتحديث كتاب
    path('books/<int:pk>/delete/', DeleteView.as_view(), name='book-delete'),  # لحذف كتاب
]
