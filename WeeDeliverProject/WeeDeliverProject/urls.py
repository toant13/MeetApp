from ProviderMenuApp import views
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.routers import DefaultRouter

admin.autodiscover()


user_list = views.UserViewSet.as_view({
    'get': 'list'
})
user_detail = views.UserViewSet.as_view({
    'get': 'retrieve'
})


# router = DefaultRouter()
# router.register(r'users', views.UserViewSet)


urlpatterns = patterns('ProviderMenuApp.views',
                       
#     url(r'^', include(router.urls)),
    
    
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
    
    
    url(r'^superadmin/', include(admin.site.urls)),
    url(r'', include('gcm.urls')),
    url(r'^item/$', views.MenuItem_list.as_view(), name='item-list'),
    url(r'^category/$', views.MenuCategory_list.as_view(), name='menuCategory-list'),
    url(r'^store/$', views.Store_list.as_view(), name='store-list'),
    url(r'^store/(?P<pk>[0-9]+)$', views.Store_Detail.as_view()),
    url(r'^device/$', views.Device_list.as_view()),

    url(r'^users/$', user_list, name='user-list'),
    url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
    
    
    url(r'^$', 'api_root'),
)


urlpatterns += format_suffix_patterns(urlpatterns)