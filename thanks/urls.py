from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^home/$', views.mainpage, name='mainpage'),
    url(r'^give_points/$', views.give_points, name='give_points'),
]
