import article.views as article
import poster.views as poster


from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login

# Uncomment the next two lines to enable the admin:
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^test/$', article.test),
    url(r'^articles/(?P<article_id>\d+)/$', article.detail),
    url(r'^form/$', article.form),
    url(r'^form/post/$', article.post),
    
    # authentication urls
    url(r'^accounts/login/$', login, {'template_name': 'login.html'}),
    url(r'^accounts/signup/$', poster.sign_up),
    url(r'^accounts/signup/post/', poster.create_user),
    
    # admin urls
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', article.headline),
)
