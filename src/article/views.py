# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse,HttpResponseRedirect,Http404
from django.shortcuts import render,get_object_or_404,redirect,get_list_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import Article,TagsArticle,Tag
from .forms import PostForm

# Create your views here.
"""
query all artical which published and paginator
"""
def allArticle(request):
    title='Way to Master'
    limit=7
    queryTag=request.GET.get("qtag")
    if queryTag=='all':
        quearyset=Article.objects.all()
    if not request.user.is_staff or not request.user.is_superuser:
        quearyset=Article.objects.filter(Publish=True).order_by("-UpdateTime")
    else:
        quearyset=Article.objects.all()

    if queryTag:
        # quearyset=quearyset.filter(Title__icontains=queryTag)
        if queryTag=='all':
            quearyset=Article.objects.filter(Publish=True).order_by("-UpdateTime")
        else:
            quearyset=getTagArticle(queryTag)

    tagset=Tag.objects.all()
    paginator = Paginator(quearyset, limit) # Show 2 contacts per page
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        contacts=paginator.page(1)
    except EmptyPage:
        contacts=paginator.page(paginator.num_pages)

    TagArray=getTags(contacts)
    rows=zip(contacts,TagArray)
    context={
    	# "form":form,
        "title":title,
        "objects_list":contacts,
        "rows":rows,
        "tagset":tagset
    }
    return render(request,"article.html",context)

"""
return all related article with one tag
"""
def getTagArticle(tag):
    allArticle=[]
    tagObj=get_object_or_404(Tag,Tags=tag)
    articles=get_list_or_404(TagsArticle,Tags=tagObj.Id)
    for i in range(len(articles)):
        allArticle.append(articles[i].Article)
    return allArticle
"""
return tages for each article，add [] if tag not exist.
"""
def getTags(array):
    AllTags=[]
    for i in array:
        current=[]
        # tags=get_list_or_404(TagsArticle,Article=i.Id)
        tags=list(TagsArticle.objects.filter(Article=i.Id))
        if tags:
            for i in range(len(tags)):
                current.append(tags[i].Tags)
        else:
            current.append([])
        AllTags.append(current)
    return AllTags


"""
query first 7 artical which published and return it to sidebar if not superuser,
else return all artical.
"""
def listArticle(request):
    limit=7
    if not request.user.is_staff or not request.user.is_superuser:
        quearyset=Article.objects.filter(Publish=True).order_by("-UpdateTime")[:limit]
    else:
        quearyset=Article.objects.all()
    context={
        "objects_list":quearyset,
    }
    return render(request,"postList.html",context)

"""
post an articals（not use change post artical in admin page）
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
    tags=getTag(obj)
    context={
        "objects":obj,
        "tags":tags
    }
    return render(request,"detail.html",context)

def getTag(obj):
    current=[]
    # tags=get_list_or_404(TagsArticle,Article=i.Id)
    tags=list(TagsArticle.objects.filter(Article=obj.Id))
    if tags:
        for i in range(len(tags)):
            current.append(tags[i].Tags)
    else:
        current.append([])
    return current

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
edit artical (not use change, edit artical in admin page）
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

"""
Ajax search result
"""


def searchResultInDetail(request, pk):
    if request.method=='GET':
        search_by=request.GET['search_by']
        if search_by is not None and search_by != u"":
            search_by=request.GET['search_by']
            statuss = Article.objects.filter(Content__contains = search_by)
        else:
            statuss = []
        context={
            'statuss':statuss,
            'searchText':search_by
        }
        return render(request, 'sideBarSearch.html', context)

def searchResult(request):
    if request.method=='GET':
        search_by=request.GET['search_by']
        if search_by is not None and search_by != u"":
            search_by=request.GET['search_by']
            statuss = Article.objects.filter(Content__contains = search_by)
        else:
            statuss = []
        context={
            'statuss':statuss,
            'searchText':search_by
        }
        return render(request, 'sideBarSearch.html', context)
