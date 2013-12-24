from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    # ex: /polls/
    url(r'^$', views.home, name='index'),
)