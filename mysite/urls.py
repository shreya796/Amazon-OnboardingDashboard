from django.conf.urls import url
from django.contrib import admin
from blog import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^post/new/$', views.post_new, name='post_new'),
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^home/$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
    url(r'^logout_view/$', views.logout_view, name='logout_view'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^operationalDashboard/$', views.login_operational_user, name='login_operational_user'),
    url(r'^register/$', views.register , name='register'),
    url(r'^search/$', views.searchResults, name='searchResults'),
]

