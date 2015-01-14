from django.conf.urls import patterns, url
from jitterbunkapp import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<user_id>\d+)/$',
                           views.userpage, name='userpage'),
                       url(r'^(?P<user_id>\d+)/add_bunk/$',
                           views.add_bunk, name='add_bunk'),)
