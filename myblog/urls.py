"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # page for end user
    path('admin/', admin.site.urls),
    # home page
    path('', include('blog.urls')),
    #path('blog/', include('blog.urls')),
    path('blog/', include('blog.urls')),



]
# 在我们创建的基础网站上，更新 /myblog/urls.py 文件。
# 以确保每当收到以blog开头的URL时，URLConf模块中的blog.urls 会处理剩余的字符串。

