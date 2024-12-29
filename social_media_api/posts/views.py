from django.shortcuts import render
from rest_framework import viewsets
from .models import Post,Comment,Like
from .serializers import PostSerializer,CommentSerializer,LikeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from accounts.models import CustomUser
from rest_framework.generics import ListAPIView
from rest_framework import permissions,status  
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.contrib.contenttypes.models import ContentType
from rest_framework.decorators import api_view
from notifications.models import  Notification
from rest_framework import generics

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

    permission_class = [permissions.IsAuthenticated]
    serializer_class = PostSerializer

    def get_queryset(self):

        currnt_user = self.request.user
        following_users = currnt_user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')

        return posts




@api_view(['POST'])
def like_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    
    like, created = Like.objects.get_or_create(
        user=request.user,
        post=post
    )
    
    if created:
        message = f"{request.user.username} liked your post!"
        Notification.objects.create(
            user=post.user,
            message=message,
        )
        return Response({"message": "Post liked successfully!"}, status=200)
    else:
        return Response({"message": "You already liked this post."}, status=400)

@api_view(['POST'])
def unlike_post(request, pk):
    post = generics.get_object_or_404(Post, pk=pk)
    
    try:
        like = Like.objects.get(
            user=request.user,
            post=post,
        )
        like.delete()
        return Response({"message": "Post unliked successfully!"}, status=200)
    except Like.DoesNotExist:
        return Response({"message": "You haven't liked this post yet."}, status=400)
    
    ["Like.objects.get_or_create(user=request.user, post=post)"]