from django.shortcuts import render
from .models import Post
# from blog.models import Post 
# Create your views here.

def list_posts_view(request):
    p = Post.objects.all()
    context = {}
    context['posts'] = p

    return render(request, "list_posts.html",context)

