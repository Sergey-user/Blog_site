from django.urls import path, include
from blog.views import *
from blog.forms import *


urlpatterns = [
    path('posts', posts_list, name='posts_list_url'),
    path('post/create', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('tags', tags_list, name='tags_list_url'),
    path('tag/create', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', tag_detail, name='tag_detail_url')
]
