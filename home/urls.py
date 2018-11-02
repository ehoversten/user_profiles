from django.conf.urls import url
# from . import views
from home.views import HomeView

app_name = 'home'

urlpatterns = [
    # url(r'^$', views.dashboard, name='dashboard'),
    url(r'^$', HomeView.as_view(), name='dashboard'),
]
