from django import forms #django already has a class called forms

from .models import Post
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Post #will follow the Post Model
        fields = ('locker_name','city','state','Pincode','capacity','ratio')


class UserForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=User
        fields=['username','email','password']
