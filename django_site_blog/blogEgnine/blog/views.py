from django.shortcuts import render, redirect
from blog.models import Post, Tag
from django.views.generic import View
from blog.forms import TagForm, PostForm
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', context={'posts':posts})


def post_detail(request, slug):
    post = Post.objects.get(slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post':post})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags})

def tag_detail(request, slug):
    tag = Tag.objects.get(slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag':tag})


class TagCreate(View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create_form.html', context={'form':form})

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create_form.html', context={'form':bound_form})


class PostCreate(View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_create_form.html', context={'form':form})

    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/post_create_form.html', context={'form':form})
