from rest_framework import serializers
from .models import Post,Comment

class CommentSerializer(serializers.ModelSerializer):

    

    class Meta:
        model = Comment
        fields = ['content','author','created_at','updated_at']


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True,read_only=True)
    class Meta:
        model = Post
        fields = ['content', 'author','comments', 'created_at','updated_at']


    def validate(self,data):
        title = data.get('title')
        
        if title and len(title) >10:
            raise serializers.ValidationError('must be longer ')
        return data
