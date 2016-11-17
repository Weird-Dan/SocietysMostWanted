from django.conf.urls import url
from . import views

app_name = "smw"

urlpatterns =[
    #url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),#homepage/preview
    url(r'^Flow/$', views.FlowView.as_view(), name='flow'),#flow view of all posts
    url(r'^Flow/(?P<pk>[0-9]+)/$', views.Cat, name='cat'),#flow view of all posts in a Category
    url(r'^Flow/cat/$', views.CategoryView.as_view(), name='categories'),#view of all categories
    url(r'^s/$', views.search, name='search'),#flow view of a search
    url(r'^(?P<pk>[0-9]+)/$', views.Idea , name='idea'),#detailed view of a post
    url(r'^create/$', views.PostCreate.as_view(), name="create"),
    url(r'^cctv/$', views.CategoryCreate.as_view(), name="cctv"),
]
