# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    """docstring forArticleAdmin."""
    list_display = ["Id","Title",
                    "updateTime",
                    "build",
                    "Publish"]
    class Meta:
        model=Article
admin.site.register(Article,ArticleAdmin)
