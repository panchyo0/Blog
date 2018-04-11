# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
# from django.contrib import messages

"""
Not only the models also the method of each model obj
"""
class Article(models.Model):
    """docstring ss Article."""
    Id=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=1000,blank = False)
    # Image=
    Publish=models.BooleanField(default=False)
    Content=models.TextField()
    updateTime=models.DateTimeField(auto_now_add=False,auto_now=True)
    build=models.DateTimeField(auto_now_add=True,auto_now=False)
    # Tag = models.ManyToManyField('Tags',through=TagsExercises)
    def __str__(self):
        """
        return  exercise Description
        """
        return str(self.Title)
    #get URL dynamic also can ues URL "article:detail" pk=obj.id
    def get_absolute_url(self):
        return reverse("article:detail",kwargs={"pk":self.Id})
