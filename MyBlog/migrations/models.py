from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    published_date = models.DateTimeField(auto_now_add=True)
    author = models.ManyToManyField(Author, null=True)
    

    #def __str__(self):
    #    return self.title
