from django.shortcuts import render
from .models import Blog, Author, Category
from django.views.generic import ListView
from django.views.generic import DetailView
from django.http import Http404


def index(request):

   # view function for home page
    
    # get all blogs and author numbs.
    num_blogs = Blog.objects.all().count()
    num_authors = Author.objects.count()
    category = Category.objects.all()
    context ={
        'num_blogs' :num_blogs,
        'num_authors': num_authors,
        'category':category,
    }
    # render the HTML template index.html with data in content
    # index is the mian page
    return render(request, 'index.html', context)


def blog_post(request):
    "shows the content of blogs"
    post_list = Blog.objects.all()
    return render(request, 'post.html', {'post_list':post_list})

def detail(request,id):
    try:
        post = Blog.objects.get(id=str(id))
    except Blog.DoesNotExist:
        raise Http404
    return render(request, 'post.html', {'post':post})

