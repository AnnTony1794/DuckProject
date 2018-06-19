from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Blog
# Create your views here.


class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog-list.html'


class BlogView(DetailView):
    model = Blog
    template_name = 'blog/blog.html'