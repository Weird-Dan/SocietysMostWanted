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
    url(r'^about', views.AboutView.as_view(), name='about'),#about
    url(r'^cmt/(?P<pk>[0-9]+)/$', views.cmt, name='comment'),
    url(r'^lk/(?P<pk>[0-9]+)/$', views.want, name='want'),
    url(r'^dk/(?P<pk>[0-9]+)/$', views.shlt, name='shlt'),
    url(r'^ud/(?P<pk>[0-9]+)/$', views.PostUpdate.as_view(), name='update_post'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostDetail.as_view(), name='post'),
    url(r'^dl/(?P<pk>[0-9]+)/$', views.delete, name='delete'),
]
