# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect

from .models import Article
from .forms import PostForm

# Create your views here.
def listArticle(request):
    quearyset=Article.objects.filter(Publish=True).order_by("-updateTime")
    context={
    	# "form":form,
        # "title":title,
        "objects_list":quearyset,
    }
    return render(request,"postList.html",context)

def createArticle(request):
    form=PostForm(request.POST or None)
    if form.is_valid():
        instance=form.save(commit=False)
        print form.cleaned_data.get("Content")
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context={
        "form":form,
        "from":"Create",
    }
    return render(request,"post.html",context)

def getArticle(request,pk):
    obj=get_object_or_404(Article,Id=pk)
    context={
        "objects":obj,
    }
    return render(request,"detail.html",context)

def deleteArticle(request,pk):
    instance=get_object_or_404(Article,Id=pk)
    instance.delete()

    return redirect("article:articleList")

def updateArticle(request,pk):
    instance=get_object_or_404(Article,Id=pk)
    form=PostForm(request.POST or None,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context={
        "form":form,
        "from":"Edit",
    }
    return render(request,"post.html",context)
