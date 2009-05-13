from django.conf.urls.defaults import *
from django.shortcuts import render_to_response, get_object_or_404
from hjemmeside.blog.models import Entry
from hjemmeside.blog.feeds import LatestEntries

info_dict = {
    'queryset' : Entry.objects.all(),
}

feeds = {
    'latest': LatestEntries,
}

urlpatterns = patterns('',
    # Example:
    # (r'^hjemmeside/', include('hjemmeside.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^$', 'hjemmeside.blog.views.list', 0),
    (r'^(?P<page>\d+)/$', 'hjemmeside.blog.views.list'),
    (r'entry/(?P<entry_id>\d+)/$', 'hjemmeside.blog.views.get_entry'),
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)

