# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings

from django.db import models
from django.core.urlresolvers import reverse
# from django.contrib import messages

class PostManager(models.Manager):
    """docstring for PostManager. rewrite origin filter"""
    def all(self,*args,**kwargs):
        return super(PostManager,self).order_by("-UpdateTime")

"""
save image according user
"""
def upload_location(instance,filename):
    return "%s/%s" %(instance.User,filename)

"""
Not only the models also the method of each model obj
"""
class Article(models.Model):
    """docstring ss Article."""
    User=models.ForeignKey(settings.AUTH_USER_MODEL,default=1)
    Id=models.AutoField(primary_key=True)
    Title=models.CharField(max_length=1000,blank = False)

    Image=models.ImageField(upload_to=upload_location,
                            null=False,
                            blank=False,
                            width_field='width_field',
                            height_field='height_field',)
    height_field=models.IntegerField(default=0)
    width_field=models.IntegerField(default=0)

    Publish=models.BooleanField(default=False)
    Content=models.TextField()
    UpdateTime=models.DateTimeField(auto_now_add=False,auto_now=True)
    Build=models.DateTimeField(auto_now_add=True,auto_now=False)
    # Tag = models.ManyToManyField('Tags',through=TagsExercises)

    #objects is build in by django, like Article.objects.all()
    objects=PostManager()
    def __str__(self):
        """
        return  exercise Description
        """
        return str(self.Title)
    #get URL dynamic also can ues URL "article:detail" pk=obj.id
    def get_absolute_url(self):
        return reverse("article:detail",kwargs={"pk":self.Id})
