from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
admin.autodiscover()
from ProviderMenuApp import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WeeDeliverProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^superadmin/', include(admin.site.urls)),
    url(r'', include('gcm.urls')),
    url(r'^item/$', 'ProviderMenuApp.views.MenuItem_list'),
    url(r'^category/$', views.MenuCategory_list.as_view()),
    url(r'^store/$', views.Store_list.as_view()),
    url(r'^device/$', views.Device_list.as_view()),
)

urlpatterns = format_suffix_patterns(urlpatterns)