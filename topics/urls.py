from django.conf.urls import patterns, url, include

urlpatterns = patterns('',
        (r'^current_datetime/$', 'topics.views.current_datetime'),
)
