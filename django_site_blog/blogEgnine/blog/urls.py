from django.urls import path, include
from blog.views import *
from blog.forms import *


urlpatterns = [
    path('posts', posts_list, name='posts_list_url'),
    path('post/create', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name='post_update_url'),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name='post_delete_url'),
    path('post/<str:slug>/', post_detail, name='post_detail_url'),
    path('tags', tags_list, name='tags_list_url'),
    path('tag/create', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/delete', TagDelete.as_view(), name='tag_delete_url'),
    path('tag/<str:slug>/update', TagUpdate.as_view(), name='tag_update_url'),
    path('tag/<str:slug>/', tag_detail, name='tag_detail_url'),
    path('category', category_list, name='category_list_url'),
    path('category/create', CategoryCreate.as_view(), name='category_create_url'),
    path('category/<str:slug>/', category_detail, name='category_detail_url')
]
