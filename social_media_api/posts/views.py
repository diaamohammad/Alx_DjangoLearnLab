from django.shortcuts import render
from rest_framework import viewsets
from .models import Post,Comment
from .serializers import PostSerializer,CommentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser
from rest_framework.generics import ListAPIView

class PostView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]  
    queryset =Post.objects.all()
    serializer_class =  PostSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['title', 'content']  
    ordering_fields = ['created_at', 'title']  
    ordering = ['created_at'] 

class CommentView(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated] 
    gueryset = Comment.objects.all()
    serializer = CommentSerializer 
    ilter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['title', 'content']  

class FeedAPIView(ListAPIView):

    permission_class = [IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):

        currnt_user = self.request.user
        following_users = currnt_user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        return posts

    
