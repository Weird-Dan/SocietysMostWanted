from django.conf.urls import url
from . import views

app_name = "userAuth"

urlpatterns =[
    url(r'^(?P<pk>[0-9]+)/$', views.UserView, name='user'),
    url(r'^login/$', views.Login, name='login'),
    url(r'^logout/$', views.Logout, name='logout'),
]
