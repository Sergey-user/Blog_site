from django import forms
from .models import *
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form_field', 'placeholder': 'Enter title'}),
            'slug': forms.TextInput(attrs={'class':'form_field', 'placeholder': 'Enter slug'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        return new_slug


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'slug', 'body', 'tags', 'category']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form_field', 'placeholder': 'Enter title'}),
            'slug': forms.TextInput(attrs={'class':'form_field', 'placeholder': 'Enter slug'}),
            'body': forms.Textarea(attrs={'class':'form_field', 'placeholder': 'Enter body', 'id':'textarea'}),
            'tags': forms.SelectMultiple(attrs={'class':'form_field', 'id':'select_tags'}),
            'category': forms.SelectMultiple(attrs={'class':'form_field', 'id':'select_tags'})

        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be "Create"')
        return new_slug


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form_field', 'placeholder': 'Enter title'}),
            'slug': forms.TextInput(attrs={'class':'form_field', 'placeholder': 'Enter slug'})
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may non be "Create"')
        return new_slug
