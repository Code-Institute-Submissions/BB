from django import forms
from .models import Post


class BlogPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'sub_title', 'content', 'image')