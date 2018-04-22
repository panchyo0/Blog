# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article
from .forms import PostForm

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    """docstring forArticleAdmin."""
    form = PostForm
    list_display = ["Id","Title",
                    "UpdateTime",
                    "Build",
                    "Publish"]
    class Meta:
        model=Article
admin.site.register(Article,ArticleAdmin)
