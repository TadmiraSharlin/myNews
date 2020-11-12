from django.conf.urls import url
from . import views

urlpatterns = [

      url(r'^comment/add/news/(?P<pk>\d+)/$', views.news_cm_add, name='news_cm_add'),
      url(r'^panel/comment/list/$', views.comments_list, name='comments_list'),
      url(r'^comment/del/(?P<pk>\d+)/$', views.comment_delete, name='comment_delete'),

]
