from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path("", views.blog_home, name="blog_home"),  # Home page for the blog
    path("post/<int:pk>/", views.post_detail, name="post_detail"),  # Post detail page
    path("create/", views.create_post, name="create_post"),  # Create post page
]
