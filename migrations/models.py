from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    published_date = models.DateTimeField()

    #def __str__(self):
    #    return self.title
