from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/?', include(admin.site.urls)),
    url(r'^test/', 'redirect.views.test', name='test'),
    url(r'^(?P<uri>.+)', 'redirect.views.redirector', name='redirector'),

)
