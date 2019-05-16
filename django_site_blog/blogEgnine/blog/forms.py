from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):

    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form_field'}),
            'slug': forms.TextInput(attrs={'class':'form_field'})
        }

        def clean_slug(self):
            new_slug = self.cleaned_data['slug'].lower()
            if new_slug == 'create':
                raise ValidationError('Slug may not be "Create"')
            return new_slug
