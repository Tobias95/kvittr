from django.conf.urls import patterns, url

from kvittr_tweets import views

urlpatterns = patterns('',
    url(r'^$', views.message_listing, name='message_listing'),
    url(r'^(\d+)/$', views.message_details, name='message_details'),
   # url(r'^(\d+)/increase_passed_exams$', views.student_increase_passed_exams, 
    #    name='student_increase_passed_exams'),   
    #url(r'^(\d+)/add_points/(\d+)$', views.student_add_points, 
     #   name='student_add_points'),   
)