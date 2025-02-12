from django.urls import path
import migrations.views as Myblog_views

url_patterns = [
    path("", Myblog_views.blog_list,name="blog_list"),
    path("<int:blog_id>/", Myblog_views.get_blog_by_id, name = "blog_details")
]