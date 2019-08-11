
from . import views
from django.urls import path
from django.conf.urls import url

urlpatterns = [
	path('', views.index, name='main-page'),
    #path('Blog_post/', views.Blog_post, name='Blog_post'),
    path('blog_post/', views.blog_post, name='post'),

]

