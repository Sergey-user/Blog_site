from django.urls import path, include
from blog.views import *


urlpatterns = [
    path('posts', posts_list, name='posts_list_url')

]
