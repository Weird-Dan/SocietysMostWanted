from django.conf.urls import url
from . import views

app_name = "attest"

urlpatterns =[
    url(r'^(?P<pk>[0-9]+)/$', views.Detail, name='detail'),
    url(r'^login/$', views.Login, name='login'),
    url(r'^lgn/$', views.lgn, name='lgn'),
    url(r'^logout/$', views.Logout, name='logout'),
    url(r'^register/$', views.Register, name='register'),
]
