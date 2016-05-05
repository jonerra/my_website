from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^message/create/$', MessageCreateView.as_view(), name='message_create'),
    url('^success/$', Success.as_view(), name='success'),
    url(r'^about/$', About.as_view(), name='about'),
    url(r'^resume/$', Resume.as_view(), name='resume'),
)