from django import forms
from .models import Post, Comment


# Form for creating and updating blog posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "body",
            "published_date",
        ]  # Add 'author' if you want users to select authors manually


# Form for submitting comments on a blog post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
