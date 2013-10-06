# -*- coding: utf-8 -*-


from django.conf.urls import patterns, include, url
import article.views as article
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^test/$', article.test),
    url(r'^articles/(?P<article_id>\d+)/$', article.detail),
    url(r'^form/$', article.form),
    url(r'^form/post/$', article.post),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', article.headline),
)
