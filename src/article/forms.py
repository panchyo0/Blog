from django import forms
from .models import Article
from pagedown.widgets import PagedownWidget
from pagedown.widgets import AdminPagedownWidget

class PostForm(forms.ModelForm):
    Content=forms.CharField(widget=AdminPagedownWidget())
    class Meta:
        """docstring Meta."""
        model=Article
        fields=[
            "Title",
            "Content",
            "Publish",
            "Image"
        ]
