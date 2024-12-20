from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from .models import Post,Comment

class CustomUserCreationForm(UserCreationForm):

    email=forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','password1','email','password2']


class PostForm(forms.ModelForm):
    
    class Meta:
        model = Post
        fields= ['title','content','published_date','author']


class CommentForm(forms.ModelForm):


    class Meta:
        model = Comment
        fields = ['content','author']
        
        def clean_content(self):
            content= self.cleaned_data.get('content')
            if len(content) < 10 :
                raise forms.ValidationError("content is short")
            return content


      