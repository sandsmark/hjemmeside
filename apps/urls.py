from django.conf.urls.defaults import *
from django.shortcuts import render_to_response, get_object_or_404
from hjemmeside.blog.models import Entry
from hjemmeside.blog.feeds import LatestEntries

urlpatterns = patterns('',
    (r'^$', 'hjemmeside.apps.views.list', 0),
    (r'^(?P<page>\d+)/$', 'hjemmeside.apps.views.list'),
    (r'app/(?P<app_id>\d+)/$', 'hjemmeside.apps.views.get_app'),
)

