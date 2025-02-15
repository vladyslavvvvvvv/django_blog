from django.shortcuts import render
from django.http import HttpRequest

import MyBlog
# Create your views here.

def posts_list(request):
    posts = MyBlog.objects.all()
    return render("post_list.html")