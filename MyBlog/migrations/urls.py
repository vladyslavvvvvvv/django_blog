from django.urls import path
import migrations.views as Myblog_views

url_patterns = [
    path("post/list/", Myblog_views.posts_list)
]