
from . import views
from django.urls import path

urlpatterns = [
	path('', views.index, name='index'),
]

urlpatterns += [

    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'),
]