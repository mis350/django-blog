from django.shortcuts import render, redirect, get_object_or_404
from django.utils.text import slugify

from django.contrib.auth.decorators import login_required


from .models import Post
# from blog.models import Post 
# Create your views here.

from .forms import PostForm, CommentForm

def list_posts_view(request):
    p = Post.objects.all()#filter(title__icontains=request.GET.get("q", ""))
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

    form = CommentForm(request.POST or None)

    print(request.POST)

    context = {}
    context['post'] = p
    context['comments'] = comments
    context['form'] = form

    if form.is_valid():
        # comment = form.save(commit=False)
        # comment.post = p
        # comment.save()
        form.save()
        return redirect('show_post_by_id', pid=p.pk)

    return render(request, 'show_post.html', context)

def search_post_view(request, q):
    p = Post.objects.filter(title__icontains=q)
    context = {}
    context['posts'] = p

    return render(request, 'list_posts.html', context)

@login_required
def create_post_view(request):

    form = PostForm(request.POST or None)
    print("*****"*20)
    print(request.POST)
    print("*****"*20)

    context = {}
    context['form'] = form
    context["title"] = "Create Post"

    if form.is_valid():
        post = form.save(commit=False)
        post.slug = slugify(post.title)
        post.save()

        return redirect('show_post_by_id', pid=post.pk)
        
    return render(request, "create_post.html", context)

def edit_post_view(request, s):
    post = get_object_or_404(Post, slug=s)
    form = PostForm(request.POST or None, instance=post)
    context = {}
    context["form"] = form
    # context["title"] = "Edit Post"

    if form.is_valid():
        post = form.save()
        return redirect('show_post_by_id', pid=post.pk)

    return render(request, 'create_post.html', context)


def delete_post_view(request, pid):
    print(f"Post to delete is {pid}")
    #Post.objects.delete(pk=pid)
    post = get_object_or_404(Post, pk=pid)
    #post = Post.objects.get(pk=pid)

    context = {}
    context["post"] = post
    if "confirm" in request.GET:
        post.delete()
        return redirect("list_post")
    elif "cancel" in request.GET:
        return redirect("list_post")
    return render(request, "confirm.html", context=context) #6
