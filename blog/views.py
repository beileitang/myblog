from django.shortcuts import render
from .models import Blog, Author, Category
from django.views.generic import ListView
from django.views.generic import DetailView


def index(request):

   # view function for home page
    
    # get all blogs and author numbs.
    num_blogs = Blog.objects.all().count()
    num_authors = Author.objects.count()
    context ={
        'num_blogs' :num_blogs,
        'num_authors': num_authors,
    }
    # render the HTML template index.html with data in content
    # index is the mian page
    return render(request, 'index.html', context=context)


def BlogDetail(request):
    "shows the content of blogs"
    blogs = Blog.objects.all()
    context = {
        'blog':blogs,
    }
    # 'blog_article/list.html' is the path of BlogDetail
    return render(request, 'blog_article/list.html', context)


"""
def Intro(request):
    author = Author.objects.all()
    context = {
        'author':authors,
    }
    # 'blog_article/list.html' is the path of BlogDetail
    return render(request, 'author.html', context)
"""



# dynamci filter
class BlogListView(ListView):
    context = 'blog'
    template_name ='blog_article/list.html'

    def get_context_data(self, **kwargs):
        # 获取原有的上下文
        context = super().get_context_data(**kwargs)
        # 增加新上下文
        context['order'] = 'total_views'
        return context


class BlogDetailView(DetailView):

    queryset = Blog.objects.all()
    context = 'blog'
    template_name ='blog_article/list.html'


