from django.urls import path, include , re_path
from . import views
from django.conf.urls import url

app_name = 'stylist'

urlpatterns = [
  # /movies/
  re_path(r'^$', views.IndexView.as_view(), name = 'index'),

  # /movies/785/
  re_path(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

  url(r'stylist/add/$', views.FreelancerCreate.as_view(), name = 'freelancer_add'),

  url(r'stylist/(?P<pk>[0-9]+)/$', views.FreelancerUpdate.as_view(), name = 'freelancer_update'),

  url(r'stylist/(?P<pk>[0-9]+)/delete/$', views.FreelancerDelete.as_view(), name = 'freelancer_delete'),




]
