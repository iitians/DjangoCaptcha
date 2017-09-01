#encoding:utf-8
from django.conf.urls import include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'^$','main.views.index'),
    url(r'^code/$','main.views.code'),
    url(r'^main/',include('main.urls')),
]
