from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^new', views.new, name="my_new"),
    url(r'^create$', views.create, name="my_create"),
    url(r'^(?P<user_number>\d+)/edit$', views.edit, name="my_edit"),
    url(r'^(?P<user_number>\d+)$', views.update, name="my_update"),
    url(r'^(?P<user_number>\d+)/destroy$', views.destroy, name="my_destroy"),
    url(r'^(?P<user_number>\d+)/show', views.show, name="my_show"),
    #url(r'^(?P<user_number>\d+)/edit$', views.edit),
]