from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import BlogPost
from django.urls import reverse_lazy

# Create your views here.

class HomePageView(ListView):
    model =  BlogPost
    template_name = 'home.html'
    context_object_name = "all_blog_posts"

class PostDetailedView(DetailView):
    model = BlogPost
    template_name = "post_detail.html"
    # context_object_name = "post_detail"

class PostCreationView(CreateView):
    model = BlogPost
    fields = ["title", "author", "body"]
    template = "blogpost_form.html"


class PostUpdateView(UpdateView):
        model = BlogPost
        fields = ["body", "title"]
        template_name = "post_edit.html"

class PostDeleteView(DeleteView):
     template_name = "post_delete.html"
     model = BlogPost
     success_url = reverse_lazy('home')