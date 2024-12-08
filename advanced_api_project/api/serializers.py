from .models import Book,Author
from rest_framework import serializers 

class Bookserializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields ='__all__'

        def validate(self, attrs):
            if attrs['publication_year'] > 2024:
                raise serializers.ValidationError("Publication year cannot be in the future")
            return attrs

class AuthorSerializer(serializers.modelserializer):

    books =Bookserializer(many=True, read_only=True)
    class Meta:
        model=Author
        fields=['name']