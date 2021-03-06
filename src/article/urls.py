from django.conf.urls import url

from .views import(
        listArticle,
        getArticle,
        deleteArticle,
        updateArticle,
        createArticle,
        searchResult,
        searchResultInDetail,
        allArticle,
        )
"""
URL rooter for artical which include List, detail, update and create.
Detail achieve by Dynamic URL binding which pass primary_key as parameter to getArticle(),name can be bind by href.
"""
urlpatterns = [
    url(r'^$',listArticle,name = "articleList"),
    url(r'^(?P<pk>\d+)/$',getArticle,name="detail"),
    url(r'^(?P<pk>\d+)/delete/$',deleteArticle,name="delete"),
    # url(r'^(?P<pk>\d+)/edit/$',updateArticle,name="edit"),
    # url(r'^create/$',createArticle),
    url(r'^ways/$',allArticle,name="allArticle"),
    # ajax search
    url(r'^ajax/$',searchResult),
    url(r'^(?P<pk>\d+)/ajax/$',searchResultInDetail),
    url(r'^ways/ajax/$',searchResult),
]
