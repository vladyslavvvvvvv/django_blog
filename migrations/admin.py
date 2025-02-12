from django.contrib import admin
from MyBlog.models import Blog # type: ignore

admin.site.register(Blog)