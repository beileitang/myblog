
from . import views
from django.urls import path

urlpatterns = [
	path('', views.index, name='main-page'),
    # blog_content/ path is views.blogDetail
    path('blog_content/', views.BlogDetail, name='Blog_page'),
    # blog_content/ path is views.blogDetail
    path('content-view/<int:pk>/', views.BlogDetailView.as_view(), name='...'),
]

