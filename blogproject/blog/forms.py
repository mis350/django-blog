from django import forms

from .models import Post, Comment

class PostForm(forms.ModelForm): #1
  class Meta: #2
    model = Post #3
    fields = ["title", "body"] #4

class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    fields = ['comment', 'author', 'email', 'post', ]