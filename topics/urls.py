from django.conf.urls import patterns, url, include
from django.views.generic import ListView
from topics.models import Person

urlpatterns = patterns('',
        (r'^current_datetime/$', 'topics.views.current_datetime'),
        (r'^contact/$', 'topics.views.contact'),
        (r'^thanks/$', 'topics.views.thanks'),
        # (r'^person/page(?P<page>[0-9]+)/$', 'person_list', Person.objects[:5]),
        (r'^upload_file/$', 'topics.views.upload_file'),
)
