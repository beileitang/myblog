from django.shortcuts import render
from .models import Blog, Author, Category
from django.views import generic

def index(request):
    """
    view function for home page
    """
    num_blogs = Blog.objects.all().count()
    num_authors = Author.objects.count()


    context ={

        'num_blogs' :num_blogs,
        'num_authors': num_authors,

    }
    # render the HTML template index.html with data in content
    return render(request, 'index.html', context=context)

class BlogDetail(generic.DetailView):
    "shows the content of blogs"

    model = Blog
    template_name = 'blog_detail.html'



