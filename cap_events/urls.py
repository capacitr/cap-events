from django.conf.urls.defaults import patterns, include, url

import views

urlpatterns = patterns('',
    url(r'^$', 'django.shortcuts.render', {"template_name" : "events.html"},  name='get_events'),
    url(r'^(?P<slug>[\w-]+)/$', views.get_event, name='get_event'),
)

