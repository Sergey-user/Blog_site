from django.shortcuts import render, redirect, reverse, get_object_or_404
from blog.models import *
from django.views.generic import View
from blog.forms import *
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/posts_list.html', context={'posts':posts})


def post_detail(request, slug):
    post = get_object_or_404(Post, slug__iexact=slug)
    return render(request, 'blog/post_detail.html', context={'post':post, 'object_for_admin':post, 'admin_detail':True})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags':tags})

def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(request, 'blog/tag_detail.html', context={'tag':tag, 'object_for_admin':tag, 'admin_detail':True})


class TagCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create_form.html', context={'form':form})
        raise_exception = True

    def post(self, request):
        bound_form = TagForm(request.POST)
        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create_form.html', context={'form':bound_form})


class TagUpdate(LoginRequiredMixin, View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(instance=tag)
        return render(request, 'blog/tag_update_form.html', context={'form':bound_form, 'tag':tag})
        raise_exception = True

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        bound_form = TagForm(request.POST, instance=tag)
        if bound_form.is_valid():
            update_tag = bound_form.save()
            return redirect(update_tag)
        return render(request, 'blog/tag_update_form.html', context={'form':bound_form, 'tag':tag})

class TagDelete(LoginRequiredMixin, View):
    def get(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        return render(request, 'blog/tag_delete_form.html', context={'tag':tag})
        raise_exception = True

    def post(self, request, slug):
        tag = Tag.objects.get(slug__iexact=slug)
        tag.delete()
        return redirect(reverse('tags_list_url'))


class PostCreate(LoginRequiredMixin, View):
    def get(self, request):
        form = PostForm()
        return render(request, 'blog/post_create_form.html', context={'form':form})
        raise_exception = True

    def post(self, request):
        bound_form = PostForm(request.POST)
        if bound_form.is_valid():
            new_post = bound_form.save()
            return redirect(new_post)
        return render(request, 'blog/post_create_form.html', context={'form':bound_form})


class PostUpdate(LoginRequiredMixin, View):
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(instance=post)
        return render(request, 'blog/post_update_form.html', context={'form':bound_form, 'post':post})
        raise_exception = True

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        bound_form = PostForm(request.POST, instance=post)
        if bound_form.is_valid():
            update_post = bound_form.save()
            return redirect(update_post)
        return render(request, 'blog/post_update_form.html')


class PostDelete(LoginRequiredMixin, View):
    def get(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        return render(request, 'blog/post_delete_form.html', context={'post':post})
        raise_exception = True

    def post(self, request, slug):
        post = Post.objects.get(slug__iexact=slug)
        post.delete()
        return redirect(reverse('posts_list_url'))


class CategoryCreate(View):
    def get(self, request):
        form = CategoryForm()
        return render(request, 'blog/category_create_form.html', context={'form':form})

    def post(self, request):
        bound_form = CategoryForm(request.POST)
        if bound_form.is_valid():
            new_category = bound_form.save()
            return redirect(new_category)
        return render(request, 'blog/category_create_form.html', context={'form':bound_form})


def category_list(request):
    category_list = Category.objects.all()
    return render(request, 'blog/category_list.html', context={'category_list':category_list})


def category_detail(request, slug):
    category = Category.objects.get(slug__iexact=slug)
    return render(request, 'blog/category_detail.html', context={'category':category})
