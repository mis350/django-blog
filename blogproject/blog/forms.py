from django import forms

from .models import Post

class PostForm(forms.ModelForm): #1
  class Meta: #2
    model = Post #3
    fields = ["title", "body"] #4