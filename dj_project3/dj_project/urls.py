"""dj_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from base import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^players/*$', views.players),
    url(r'^base$', views.base),
    url(r'^players$', views.players),
    url(r'^accounts/login/$', auth_views.login),
    url(r"^players/change_exp/*", views.players_change_exp),
    url(r"^players_change_exp/*", views.players_change_exp),
    url(r'^accounts/logout/$', auth_views.logout),
    url(r'^logout/$', views.logout_view)
]