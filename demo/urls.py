from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'demo.views.home', name='home'),
    url(r'^newsletters/', include('newsletters.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^notification/', include('notification.urls')),
)
