from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^news/(?P<pk>\d+)/$', views.news_details, name='news_details'),
    url(r'^panel/news/list/$', views.news_list, name='news_list'),
    url(r'^panel/news/add/$', views.news_add, name='news_add'),
    url(r'^panel/news/del/(?P<pk>\d+)/$', views.news_delete, name='news_delete'),
    url(r'^panel/news/edit/(?P<pk>\d+)/$', views.news_edit, name='news_edit'),
    url(r'^panel/news/publish/(?P<pk>\d+)/$', views.news_publish, name='news_publish'),
    url(r'^panel/news/unpublish/(?P<pk>\d+)/$', views.news_unpublish, name='news_unpublish'),

]
