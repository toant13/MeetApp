from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WeeDeliverProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^gadmin/', include(admin.site.urls)),
    url(r'', include('gcm.urls')),
)
