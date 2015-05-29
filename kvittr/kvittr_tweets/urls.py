from django.conf.urls import patterns, url

from kvittr_tweets import views

urlpatterns = patterns('',
    url(r'^$', views.message_listing, name='message_listing'),
    url(r'^(\d+)/$', views.message_details, name='message_details'),
 