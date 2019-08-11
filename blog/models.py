from django.db import models


class Category(models.Model):
    """
    category: name
    """
    id = models.IntegerField(primary_key=True)
    # fields: rep. a columns of data
    name = models.CharField(max_length=50, help_text="Enter the category's name")

    def __str__(self):
        """string for rep. the category"""
        return self.name


class Blog(models.Model):
    """
    blog class: author, body, date, category and tag
    """
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    body = models.TextField()
    date = models.DateField()
    """Foreign Key: one to many relationship, one category can have many blogs """
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    """Foreign Key: one to many relationship, one author can have many blogs """
    Author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)

    class Meta:
        ordering = ['date']

    def __str__(self):
        return self.title




class Author(models.Model):
    first_name = models.CharField(max_length=10)
    last_name = models.CharField(max_length=10)

    class Meta:
        ordering = ['last_name']

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'