from django.shortcuts import render
from django.views.generic import ListView
from .models import Post

# Create your views here.

class PostView(ListView):
    model = Post
    template = 'home.html'
    context_object_name = 'all_post_list'