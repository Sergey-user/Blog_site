from django.shortcuts import render
from blog.models import Post
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', context={'posts':posts})

def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post':post})
