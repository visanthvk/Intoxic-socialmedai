from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^update/(?P<email>.*)$',views.update),
    url(r'(?P<email>.*)', views.index, name='index'),
]