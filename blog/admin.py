from django.contrib import admin

# Register your models here.

from  .models import Blog,Author,Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title','Author','category','date')
    search_fields = ['title','body']



class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name','last_name')
    search_fields = ['first_name','last_name']

admin.site.register(Blog,BlogAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category)
