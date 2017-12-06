from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^events/(?P<eventid>\d+/)$', views.event, name='event')
]