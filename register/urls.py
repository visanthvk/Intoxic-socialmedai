from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.index),
    url('registeruser',views.register),
    url('login', views.login)
]