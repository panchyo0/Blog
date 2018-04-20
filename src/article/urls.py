from django.conf.urls import url

from .views import(
        listArticle,
        getArticle,
        deleteArticle,
        updateArticle,
        createArticle,
        searchResultInMain,
        searchResultInDetail,
        )
"""
URL rooter for artical which include List, detail, update and create.
Detail achieve by Dynamic URL binding which pass primary_key as parameter to getArticle(),name can be bind by href.
"""
urlpatterns = [
    url(r'^$',listArticle,name = "articleList"),
    url(r'^(?P<pk>\d+)/$',getArticle,name="detail"),
    url(r'^(?P<pk>\d+)/delete/$',deleteArticle,name="delete"),
    url(r'^(?P<pk>\d+)/edit/$',updateArticle,name="edit"),
    url(r'^create/$',createArticle),
    
    # ajax search
    url(r'^ajax/$',searchResultInMain),
    url(r'^(?P<pk>\d+)/ajax/$',searchResultInDetail),
]
