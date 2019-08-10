from django.db import models


class Category(models.Model):
    """
    category: name
    """
    # fields: rep. a columns of data
    name = models.CharField(max_length=50, help_text="Enter the category's name")

    def __str__(self):
        """string for rep. the category"""
        return self.name

from django.urls import reverse # Used to generate URLs by reversing the URL patterns

class Blog(models.Model):
    """
    blog class: author, body, date, category and tag
    """
    title = models.CharField(max_length=50)
    body = models.TextField()
    isbn = models.CharField('ISBN', max_length=20,help_text='20 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    date = models.DateField()
    """Foreign Key: one to many relationship, one category can have many blogs """
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    """Foreign Key: one to many relationship, one author can have many blogs """
    Author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ url to the details fo blogs"""
        return reverse('blog_details', args=[self(self.id)])


class Author(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author_details', args=[str(self.id)])

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'