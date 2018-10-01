'''learnings的自定URL'''
from django.conf.urls import url
from . import views

app_name = 'learnings'

urlpatterns = [
    #index主页
    url('^$',views.index,name='index'),
    url('^topics/$',views.topics,name='topics'),
    url('^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    url('^new_topic/$',views.new_topic,name='new_topic'),
    url(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),
    url(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,name='edit_entry'),
]