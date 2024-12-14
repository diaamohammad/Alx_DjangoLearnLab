from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):

    email=forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username','password1','email','password2']