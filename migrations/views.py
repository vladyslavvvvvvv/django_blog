from django.shortcuts import render
from MyBlog.models import Blog  # type: ignore
# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all()
    context = {
            "blog_list": blogs,
    }
    return render(
        request,
        template_name="MyBlog/blog_list.html",
        context=context
    )