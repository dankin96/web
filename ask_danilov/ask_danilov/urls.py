"""ask_danilov URL Configuration

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
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^(?P<page>\d+)/$', 'ask.views.index', name='index'),
    url(r'^$', 'ask.views.index', name='index'),
    url(r'^hot/(?P<page>\d+)/$', 'ask.views.hot_index', name='hot_index'),
    url(r'^hot/$', 'ask.views.hot_index', name='hot_index'),
    url(r'^tag/(?P<tag>\w+)/(?P<page>\d+)/$', 'ask.views.tag_index', name='tag_index'),
    url(r'^tag/(?P<tag>\w+)/$', 'ask.views.tag_index', name='tag_index'),
    url(r'^question/(?P<id>\d+)/(?P<page>\d+)/$', 'ask.views.answers', name='answers'),
    url(r'^question/(?P<id>\d+)/$', 'ask.views.answers', name='answers'),
    url(r'^login/$', 'ask.views.login', name='login'),
    url(r'^signup/$', 'ask.views.signup', name='signup'),
    url(r'^ask/$', 'ask.views.ask', name='ask'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
