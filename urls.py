from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^hjemmeside/', include('hjemmeside.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^blog/', include('hjemmeside.blog.urls')),
    (r'^apps/', include('hjemmeside.apps.urls')),
    # (r'^gallery/', include('hjemmeside.gallery.urls')),
    # (r'^polls/', include('hjemmeside.polls.urls')),
    (r'^admin/(.*)', admin.site.root),
    (r'^gallery/', include('photologue.urls')),
    (r'^$', 'django.views.generic.simple.direct_to_template', { 'template' : 'base.html'}),
)

