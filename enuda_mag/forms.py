from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.forms import TextInput
from django import forms
from .models import Image, BlogPost

class CreateUserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']

class UserLoginForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']


class UserImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ['image']


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = ['content']
