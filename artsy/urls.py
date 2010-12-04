from django.conf.urls.defaults import patterns, url

from artsy import views

urlpatterns = patterns('',
	url(r'^$', views.project_index, name='project_index'),
    url(r'^project/(?P<slug>(\w|-)+)/$', views.project_detail, name='project_detail'),
	url(r'^category/(?P<slug>\w+)/$', views.category_index, name='category_index'),
)

