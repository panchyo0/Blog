from django import forms
from .models import Article

class PostForm(forms.ModelForm):
    class Meta:
        """docstring Meta."""
        model=Article
        fields=[
            "Title",
            "Content",
            "Publish",
        ]
