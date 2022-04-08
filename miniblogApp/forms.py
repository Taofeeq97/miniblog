from django import forms

from .models import blogentry

class blogForm(forms.ModelForm):
    class Meta:
        model=blogentry
        fields=('blog_title','blog_header', 'blog_content')