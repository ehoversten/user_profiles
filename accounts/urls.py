from django.conf.urls import url
from django.contrib.auth.views import login, logout
from . import views

app_name = 'accounts'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', login, {'template_name': 'accounts/login.html'}, name='login'),
    url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
    url(r'^register/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),
]
