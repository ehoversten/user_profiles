from django.conf.urls import url
# from . import views
from home.views import HomeView
from . import views

# app_name = 'home'

urlpatterns = [
    # url(r'^$', views.dashboard, name='dashboard'),
    url(r'^$', HomeView.as_view(), name='dashboard'),
    url(r'^connect/(?P<operation>.+)/(?P<pk>\d+)/$', views.change_friends, name='change_friends')
]
