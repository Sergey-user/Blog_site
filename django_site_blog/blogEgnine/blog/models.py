from django.db import models
from django.shortcuts import reverse
# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50, db_index=True)
    slug = models.SlugField(max_length=50, db_index=True, unique=True)
    body = models.TextField(blank=True, db_index=True)
    datetime = models.DateTimeField(auto_now_add=True)
    tags = models.ManyToManyField('Tag', blank=True, related_name='posts')


    def get_absolute_url(self):
        return reverse('post_detail_url', kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('post_update_url', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('post_delete_url', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title

class Tag(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('tag_update_url', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('tag_delete_url', kwargs={'slug':self.slug})

    def __str__(self):
        return self.title
