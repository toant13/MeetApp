from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
admin.autodiscover()
from ProviderMenuApp import views
from django.conf.urls import include

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'WeeDeliverProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^superadmin/', include(admin.site.urls)),
    url(r'', include('gcm.urls')),
    url(r'^item/$', views.MenuItem_list.as_view()),
    url(r'^category/$', views.MenuCategory_list.as_view()),
    url(r'^store/$', views.Store_list.as_view()),
    url(r'^store/(?P<pk>[0-9]+)$', views.Store_Detail.as_view()),
    url(r'^device/$', views.Device_list.as_view()),
    
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
    
    
)

urlpatterns += patterns('',
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
)
urlpatterns = format_suffix_patterns(urlpatterns)