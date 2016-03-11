from django.conf.urls import url
from django.conf import settings

from . import views

app_name = 'userprofile'
urlpatterns = [
    url(r'^user/(?P<pk>[0-9]+)/$', views.ProfileView.as_view(), name='profile'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.PostView.as_view(), name='post'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
             {'document_root': settings.MEDIA_ROOT}),   
    url(r'^$', views.HomeView, name='home'),

]