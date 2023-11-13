from django.shortcuts import render
from .models import Post
# from blog.models import Post 
# Create your views here.

def list_posts_view(request):
    p = Post.objects.filter(status=0)
    context = {}
    context['posts'] = p

    return render(request, "list_posts.html",context)

def show_post_view(request, pid):
    p = Post.objects.get(pk=pid)
    comments = p.comment_set.all()
    context = {}
    context['post'] = p
    context['comments'] = comments
    return render(request, 'show_post.html', context)

def show_post_slug_view(request, s):
    p = Post.objects.get(slug=s)
    comments = p.comment_set.all()
    context = {}
    context['post'] = p
    context['comments'] = comments
    return render(request, 'show_post.html', context)
