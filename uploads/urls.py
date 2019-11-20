from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('about/', views.about, name='about'),
    url('contact/', views.contact, name='contact'),
    url('koziorozec/', views.koziorozec, name='koziorozec'),
    url('wodnik/', views.wodnik, name='wodnik'),
    url('ryby/', views.ryby, name='ryby'),
    url('baran/', views.baran, name='baran'),
    url('byk/', views.byk, name='byk'),
    url('bliznieta/', views.bliznieta, name='bliznieta'),
    



]
