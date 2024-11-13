# forms.py
from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['name', 'description', 'attachment']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 5}),
        }
