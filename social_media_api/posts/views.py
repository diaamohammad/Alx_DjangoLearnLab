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
from rest_framework.views import APIView


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



class LikePostView(APIView):

    permission_class = [IsAuthenticated]

    def post(self,request,post_id):
        post=get_object_or_404(Post,id=post_id)
        content_type = ContentType.objects.get_for_model(post)

        if Like.objects.filter(user=request.user,content_type=content_type,object_id=post.id).exists():

        
            return Response({'message': 'you liked this post befor'}, status=status.HTTP_400_BAD_REQUEST)
        
        Like.objects.create(user=request.user,content_type=content_type,object_id=post.id)

        return Response({'message': 'already liked'}, status=status.HTTP_200_OK)
        
class UnlikePostView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, post_id):
        
        post = get_object_or_404(Post, id=post_id)
        content_type = ContentType.objects.get_for_model(post)

        like = Like.objects.filter(user=request.user, content_type=content_type, object_id=post.id).first()
        
        if not like:
            return Response({'message': 'you dont liked this post'}, status=status.HTTP_400_BAD_REQUEST)

        
        Like.delete()

        

        return Response({'message': 'the post has been disliked'}, status=status.HTTP_200_OK)



