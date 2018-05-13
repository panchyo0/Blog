# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Article,Tag,TagsArticle
from .forms import PostForm

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    """docstring forArticleAdmin."""
    form = PostForm
    list_display = ["Id",
                    "Title",
                    "all_Tags",
                    "UpdateTime",
                    "Build",
                    "Counter",
                    "Publish"]
    class Meta:
        model=Article
    def all_Tags(self,obj):
        return "\n".join([p.Tags for p in obj.Tags.all()])
admin.site.register(Article,ArticleAdmin)

class TagAdmin(admin.ModelAdmin):
    """docstring for Tag."""
    list_display = ['Id',
                    'Tags']
    list_filter = ["Tags"]
    search_fields = ["Tags"]
admin.site.register(Tag, TagAdmin)


#Add question for questionnaire
class TagsArticleAdmin(admin.ModelAdmin):
    list_display = ['Article',
                    'Tags']
    list_filter = ["Tags"]
    search_fields = ["Tags",
                     "Article"]
admin.site.register(TagsArticle, TagsArticleAdmin)
