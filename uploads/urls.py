from django.conf.urls import url
from django.contrib import admin

from uploads.core import views


urlpatterns = [
    url('^$', views.home, name='home'),
    url('about/', views.about, name='about'),
    url('authors/', views.authors, name='authors'),
    url('koziorozec/', views.koziorozec, name='koziorozec'),
    url('wodnik/', views.wodnik, name='wodnik'),
    url('ryby/', views.ryby, name='ryby'),
    url('baran/', views.baran, name='baran'),
    url('byk/', views.byk, name='byk'),
    url('bliznieta/', views.bliznieta, name='bliznieta'),
    url('rak/', views.rak, name='rak'),
    url('lew/', views.lew, name='lew'),
    url('panna/', views.panna, name='panna'),
    url('waga/', views.waga, name='waga'),
    url('skorpion/', views.skorpion, name='skorpion'),
    url('strzelec/', views.strzelec, name='strzelec'),
]
