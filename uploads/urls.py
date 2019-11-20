from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('about/', views.about, name='about'),
    url('contact/', views.contact, name='contact'),
    url('koziorozec/', views.koziorozec, name='koziorozec')
    ]
