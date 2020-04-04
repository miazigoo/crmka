from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['']
        verbose_name = 'ModelPost'
        verbose_name_plural = 'ModelPosts'