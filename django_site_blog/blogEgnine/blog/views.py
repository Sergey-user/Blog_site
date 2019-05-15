from django.shortcuts import render
from blog.models import Post
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', context={'posts':posts})
