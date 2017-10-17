from django.conf.urls import url
from . import views           # This line is new!
urlpatterns=[
    url(r'^$', views.index),   # This line has changed!
    url(r'^new/$', views.new),
    url(r'^create/$', views.create),
    url(r'^(?P<blogId>[0-9]{2})/$', views.show),
    url(r'^(?P<blogId>[0-9]{2})/edit/$', views.edit),
    url(r'^(?P<blogId>[0-9]{2})/delete/$', views.destroy)

]