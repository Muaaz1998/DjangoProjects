from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import BlogPost

# Create your views here.

class HomePageView(ListView):
    model =  BlogPost
    template_name = 'home.html'
    context_object_name = "all_blog_posts"

class PostDetailedView(DetailView):
    model = BlogPost
    template_name = "post_detail.html"
    # context_object_name = "post_detail"
    

