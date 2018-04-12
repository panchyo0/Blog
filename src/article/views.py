# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404,redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article
from .forms import PostForm

# Create your views here.
"""
query all artical which published and paginator
"""
def listArticle(request):
    if not request.user.is_staff or not request.user.is_superuser:
        quearyset=Article.objects.filter(Publish=True).order_by("-UpdateTime")
    else:
        quearyset=Article.objects.all()
    paginator = Paginator(quearyset, 7) # Show 2 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts=paginator.page(1)
    except EmptyPage:
        contacts=paginator.page(paginator.num_pages)
    context={
    	# "form":form,
        # "title":title,
        "objects_list":contacts,
    }
    return render(request,"postList.html",context)

"""
post an articals
"""
def createArticle(request):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    form=PostForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        instance=form.save(commit=False)
        # print form.cleaned_data.get("Content")
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context={
        "form":form,
        "from":"Create",
    }
    return render(request,"post.html",context)

"""
show detail of artiacal
"""
def getArticle(request,pk):
    obj=get_object_or_404(Article,Id=pk)
    context={
        "objects":obj,
    }
    return render(request,"detail.html",context)

"""
delete articals
"""
def deleteArticle(request,pk):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(Article,Id=pk)
    instance.delete()

    return redirect("article:articleList")

"""
edit artical
"""
def updateArticle(request,pk):
    if not request.user.is_staff or not request.user.is_superuser:
        raise Http404
    instance=get_object_or_404(Article,Id=pk)
    form=PostForm(request.POST or None,request.FILES or None,instance=instance)
    if form.is_valid():
        instance=form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context={
        "form":form,
        "from":"Edit",
    }
    return render(request,"post.html",context)
